# -*- coding: utf-8 -*-
# Copyright 2020, CS GROUP - France, http://www.c-s.fr
#
# This file is part of EODAG project
#     https://www.github.com/CS-SI/EODAG
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Miscellaneous utilities to be used throughout eodag.

Everything that does not fit into one of the specialised categories of utilities in
this package should go here
"""
from __future__ import unicode_literals

import copy
import errno
import os
import re
import string
import sys
import types
import unicodedata
from datetime import datetime
from itertools import repeat, starmap

import click
import six
from rasterio.crs import CRS
from requests.auth import AuthBase
from tqdm import tqdm
from tqdm.notebook import tqdm as tqdm_notebook
from unidecode import unidecode

# All modules using these should import them from utils package
try:  # PY3
    from urllib.parse import urljoin, urlparse, parse_qs, urlunparse  # noqa
except ImportError:  # PY2
    from urlparse import urljoin, urlparse, parse_qs, urlunparse  # noqa

try:  # PY3
    from urllib.parse import quote, quote_plus  # noqa

    if sys.version_info.minor < 5:
        # Explicitly redefining urlencode the way it is defined in Python 3.5
        def urlencode(
            query,
            doseq=False,
            safe="",
            encoding=None,
            errors=None,
            quote_via=quote_plus,
        ):  # noqa
            """Encode a dict or sequence of two-element tuples into a URL query string.

            If any values in the query arg are sequences and doseq is true, each
            sequence element is converted to a separate parameter.

            If the query arg is a sequence of two-element tuples, the order of the
            parameters in the output will match the order of parameters in the
            input.

            The components of a query arg may each be either a string or a bytes type.

            The safe, encoding, and errors parameters are passed down to the function
            specified by quote_via (encoding and errors only if a component is a str).
            """

            if hasattr(query, "items"):
                query = query.items()
            else:
                # It's a bother at times that strings and string-like objects are
                # sequences.
                try:
                    # non-sequence items should not work with len()
                    # non-empty strings will fail this
                    if len(query) and not isinstance(query[0], tuple):
                        raise TypeError
                    # Zero-length sequences of all types will get here and succeed,
                    # but that's a minor nit.  Since the original implementation
                    # allowed empty dicts that type of behavior probably should be
                    # preserved for consistency
                except TypeError:
                    ty, va, tb = sys.exc_info()
                    raise TypeError(
                        "not a valid non-string sequence " "or mapping object"
                    ).with_traceback(tb)

            l = []  # noqa
            if not doseq:
                for k, v in query:
                    if isinstance(k, bytes):
                        k = quote_via(k, safe)
                    else:
                        k = quote_via(str(k), safe, encoding, errors)

                    if isinstance(v, bytes):
                        v = quote_via(v, safe)
                    else:
                        v = quote_via(str(v), safe, encoding, errors)
                    l.append(k + "=" + v)
            else:
                for k, v in query:
                    if isinstance(k, bytes):
                        k = quote_via(k, safe)
                    else:
                        k = quote_via(str(k), safe, encoding, errors)

                    if isinstance(v, bytes):
                        v = quote_via(v, safe)
                        l.append(k + "=" + v)
                    elif isinstance(v, str):
                        v = quote_via(v, safe, encoding, errors)
                        l.append(k + "=" + v)
                    else:
                        try:
                            # Is this a sufficient test for sequence-ness?
                            x = len(v)  # noqa
                        except TypeError:
                            # not a sequence
                            v = quote_via(str(v), safe, encoding, errors)
                            l.append(k + "=" + v)
                        else:
                            # loop over the sequence
                            for elt in v:
                                if isinstance(elt, bytes):
                                    elt = quote_via(elt, safe)
                                else:
                                    elt = quote_via(str(elt), safe, encoding, errors)
                                l.append(k + "=" + elt)
            return "&".join(l)

    else:
        from urllib.parse import urlencode


except ImportError:  # PY2
    from urllib import quote, quote_plus  # noqa

    # Explicitly redefining urlencode the way it is defined in Python 3.5
    def urlencode(
        query, doseq=False, safe="", encoding=None, errors=None, quote_via=quote_plus
    ):
        """Encode a dict or sequence of two-element tuples into a URL query string.

        If any values in the query arg are sequences and doseq is true, each
        sequence element is converted to a separate parameter.

        If the query arg is a sequence of two-element tuples, the order of the
        parameters in the output will match the order of parameters in the
        input.

        The components of a query arg may each be either a string or a bytes type.

        The safe, encoding, and errors parameters are passed down to the function
        specified by quote_via (encoding and errors only if a component is a str).
        """

        if hasattr(query, "items"):
            query = query.items()
        else:
            # It's a bother at times that strings and string-like objects are
            # sequences.
            try:
                # non-sequence items should not work with len()
                # non-empty strings will fail this
                if len(query) and not isinstance(query[0], tuple):
                    raise TypeError
                # Zero-length sequences of all types will get here and succeed,
                # but that's a minor nit.  Since the original implementation
                # allowed empty dicts that type of behavior probably should be
                # preserved for consistency
            except TypeError:
                ty, va, tb = sys.exc_info()
                raise TypeError(
                    "not a valid non-string sequence " "or mapping object"
                ).with_traceback(tb)

        l = []  # noqa
        if not doseq:
            for k, v in query:
                if isinstance(k, bytes):
                    k = quote_via(k, safe)
                else:
                    k = quote_via(str(k), safe)

                if isinstance(v, bytes):
                    v = quote_via(v, safe)
                else:
                    v = quote_via(str(v), safe)
                l.append(k + "=" + v)
        else:
            for k, v in query:
                if isinstance(k, bytes):
                    k = quote_via(k, safe)
                else:
                    k = quote_via(str(k), safe)

                if isinstance(v, bytes):
                    v = quote_via(v, safe)
                    l.append(k + "=" + v)
                elif isinstance(v, six.string_types):
                    v = quote_via(v, safe)
                    l.append(k + "=" + v)
                else:
                    try:
                        # Is this a sufficient test for sequence-ness?
                        x = len(v)  # noqa
                    except TypeError:
                        # not a sequence
                        v = quote_via(str(v), safe)
                        l.append(k + "=" + v)
                    else:
                        # loop over the sequence
                        for elt in v:
                            if isinstance(elt, bytes):
                                elt = quote_via(elt, safe)
                            else:
                                elt = quote_via(str(elt), safe)
                            l.append(k + "=" + elt)
        return "&".join(l)


class RequestsTokenAuth(AuthBase):
    """A custom authentication class to be used with requests module"""

    def __init__(self, token, where, qs_key=None):
        self.token = token
        self.where = where
        self.qs_key = qs_key

    def __call__(self, request):
        """Perform the actual authentication"""
        if self.where == "qs":
            parts = urlparse(request.url)
            qs = parse_qs(parts.query)
            qs[self.qs_key] = self.token
            request.url = urlunparse(
                (
                    parts.scheme,
                    parts.netloc,
                    parts.path,
                    parts.params,
                    urlencode(qs),
                    parts.fragment,
                )
            )
        elif self.where == "header":
            request.headers["Authorization"] = "Bearer {}".format(self.token)
        return request


class FloatRange(click.types.FloatParamType):
    """A parameter that works similar to :data:`click.FLOAT` but restricts the
    value to fit into a range. Fails if the value doesn't fit into the range.
    """

    name = "percentage"

    def __init__(self, min=None, max=None):
        self.min = min
        self.max = max

    def convert(self, value, param, ctx):
        """Convert value"""
        rv = click.types.FloatParamType.convert(self, value, param, ctx)
        if (
            self.min is not None
            and rv < self.min
            or self.max is not None
            and rv > self.max
        ):
            if self.min is None:
                self.fail(
                    "%s is bigger than the maximum valid value " "%s." % (rv, self.max),
                    param,
                    ctx,
                )
            elif self.max is None:
                self.fail(
                    "%s is smaller than the minimum valid value "
                    "%s." % (rv, self.min),
                    param,
                    ctx,
                )
            else:
                self.fail(
                    "%s is not in the valid range of %s to %s."
                    % (rv, self.min, self.max),
                    param,
                    ctx,
                )
        return rv

    def __repr__(self):
        return "FloatRange(%r, %r)" % (self.min, self.max)


def slugify(value, allow_unicode=False):
    """Copied from Django Source code, only modifying last line (no need for safe
    strings).
    source: https://github.com/django/django/blob/master/django/utils/text.py

    Convert to ASCII if 'allow_unicode' is False. Convert spaces to hyphens.
    Remove characters that aren't alphanumerics, underscores, or hyphens.
    Convert to lowercase. Also strip leading and trailing whitespace.
    """
    try:  # PY2
        value = unicode(value)
    except NameError:  # PY3
        value = str(value)
    if allow_unicode:
        value = unicodedata.normalize("NFKC", value)
    else:
        value = (
            unicodedata.normalize("NFKD", value)
            .encode("ascii", "ignore")
            .decode("ascii")
        )
    value = re.sub(r"[^\w\s-]", "", value).strip().lower()
    return re.sub(r"[-\s]+", "-", value)


def utf8_everywhere(mapping):
    """Recursively transforms all string found in the dict mapping to UTF-8 if we are
    on Python 2"""
    mutate_dict_in_place(
        (
            lambda value: value.decode("utf-8")
            if isinstance(value, str)
            and sys.version_info.major == 2
            and sys.version_info.minor == 7
            else value
        ),
        mapping,
    )


def sanitize(value):
    """Sanitize string to be used as a name of a directory.
    >>> sanitize('productName')
    'productName'
    >>> sanitize('name with multiple  spaces')
    'name_with_multiple_spaces'
    >>> sanitize('âtre fête île alcôve bûche çà génèse où Noël ovoïde capharnaüm')
    'atre_fete_ile_alcove_buche_ca_genese_ou_Noel_ovoide_capharnaum'
    >>> sanitize('replace,ponctuation:;signs!?byunderscorekeeping-hyphen.dot_and_underscore')   # noqa
    'replace_ponctuation_signs_byunderscorekeeping-hyphen.dot_and_underscore'
    """
    # remove accents
    rv = unidecode(value)
    # replace punctuation signs and spaces by underscore
    # keep hyphen, dot and underscore from punctuation
    tobereplaced = re.sub(r"[-_.]", "", string.punctuation)
    # add spaces to be removed
    tobereplaced += r"\s"

    rv = re.sub(r"[" + tobereplaced + r"]+", "_", rv)
    return str(rv)


def mutate_dict_in_place(func, mapping):
    """Apply func to values of mapping.

    The mapping object's values are modified in-place. The function is recursive,
    allowing to also modify values of nested dicts that may be level-1 values of
    mapping.

    :param func: A function to apply to each value of mapping which is not a dict object
    :type func: func
    :param mapping: A Python dict object
    :type mapping: dict
    :returns: None
    """
    for key, value in mapping.items():
        if isinstance(value, dict):
            mutate_dict_in_place(func, value)
        else:
            mapping[key] = func(value)


def merge_mappings(mapping1, mapping2):
    """Merge two mappings with string keys, values from `mapping2` overriding values
    from `mapping1`.

    Do its best to detect the key in `mapping1` to override. For example, let's say
    we have::

        mapping2 = {"keya": "new"}
        mapping1 = {"keyA": "obsolete"}

    Then::

        merge_mappings(mapping1, mapping2) ==> {"keyA": "new"}

    If mapping2 has a key that cannot be detected in mapping1, this new key is added
    to mapping1 as is.

    :param dict mapping1: The mapping containing values to be overridden
    :param dict mapping2: The mapping containing values that will override the
                          first mapping
    """
    # A mapping between mapping1 keys as lowercase strings and original mapping1 keys
    m1_keys_lowercase = {key.lower(): key for key in mapping1}
    for key, value in mapping2.items():
        if isinstance(value, dict):
            try:
                merge_mappings(mapping1[key], value)
            except KeyError:
                # If the key from mapping2 is not in mapping1, it is either key is
                # the lowercased form of the corresponding key in mapping1 or because
                # key is a new key to be added in mapping1
                current_value = mapping1.setdefault(m1_keys_lowercase.get(key, key), {})
                if not current_value:
                    current_value.update(value)
                else:
                    merge_mappings(current_value, value)
        else:
            # Even for "scalar" values (a.k.a not nested structures), first check if
            # the key from mapping1 is not the lowercase version of a key in mapping2.
            # Otherwise, create the key in mapping1. This is the meaning of
            # m1_keys_lowercase.get(key, key)
            current_value = mapping1.get(m1_keys_lowercase.get(key, key), None)
            if current_value is not None:
                current_value_type = type(current_value)
                if isinstance(value, six.string_types):
                    # Bool is a type with special meaning in Python, thus the special
                    # case
                    if current_value_type is bool:
                        if value.capitalize() not in ("True", "False"):
                            raise ValueError(
                                "Only true or false strings (case insensitive) are "
                                "allowed for booleans"
                            )
                        # Get the real Python value of the boolean. e.g: value='tRuE'
                        # => eval(value.capitalize())=True.
                        # str.capitalize() transforms the first character of the string
                        # to a capital letter
                        mapping1[m1_keys_lowercase[key]] = eval(value.capitalize())
                    else:
                        mapping1[m1_keys_lowercase[key]] = current_value_type(value)
                else:
                    try:
                        mapping1[m1_keys_lowercase[key]] = current_value_type(value)
                    except TypeError:
                        # Ignore any override value that does not have the same type
                        # as the default value
                        pass
            else:
                mapping1[key] = value


def maybe_generator(obj):
    """Generator function that get an arbitrary object and generate values from it if
    the object is a generator."""
    if isinstance(obj, types.GeneratorType):
        for elt in obj:
            yield elt
    else:
        yield obj


DEFAULT_PROJ = CRS.from_epsg(4326)


def get_timestamp(date_time, date_format="%Y-%m-%dT%H:%M:%S"):
    """Returns the given date_time string formatted with date_format as timestamp,
    in a PY2/3 compatible way

    :param date_time: the datetime string to return as timestamp
    :type date_time: str or unicode
    :param date_format: (optional) the date format in which date_time is given,
                        defaults to '%Y-%m-%dT%H:%M:%S'
    :type date_format: str or unicode
    :returns: the timestamp corresponding to the date_time string in seconds
    :rtype: float
    """
    date_time = datetime.strptime(date_time, date_format)
    try:
        return date_time.timestamp()
    # There is no timestamp method on datetime objects in Python 2
    except AttributeError:
        import time

        return time.mktime(date_time.timetuple()) + date_time.microsecond / 1e6


class ProgressCallback(object):
    """A callable used to render progress to users for long running processes"""

    def __init__(self, max_size=None):
        self.pb = None
        self.max_size = max_size

    def __call__(self, current_size, max_size=None):
        """Update the progress bar.

        :param current_size: amount of data already processed
        :type current_size: int
        :param max_size: maximum amount of data to be processed
        :type max_size: int
        """
        if max_size is not None:
            self.max_size = max_size
        if self.pb is None:
            self.pb = tqdm(total=self.max_size, unit="B", unit_scale=True)
        self.pb.update(current_size)


class NotebookProgressCallback(ProgressCallback):
    """A custom progress bar to be used inside Jupyter notebooks"""

    def __call__(self, current_size, max_size=None):
        """Update the progress bar"""
        if max_size is not None:
            self.max_size = max_size
        if self.pb is None:
            self.pb = tqdm_notebook(total=self.max_size, unit="B", unit_scale=True)
        self.pb.update(current_size)


def repeatfunc(func, n, *args):
    """Call `func` `n` times with `args`"""
    return starmap(func, repeat(args, n))


def makedirs(dirpath):
    """Create a directory in filesystem with parents if necessary"""
    try:
        os.makedirs(dirpath)
    except OSError as err:
        # Reraise the error unless it's about an already existing directory
        if err.errno != errno.EEXIST or not os.path.isdir(dirpath):
            raise


def update_nested_dict(old_dict, new_dict, extend_list_values=False):
    """Update recursively old_dict items with new_dict ones

    :param old_dict: dict to be updated
    :type old_dict: dict
    :param new_dict: incomming dict
    :type new_dict: dict
    :param extend_list_values: extend old_dict value if both old/new values are lists
    :type extend_list_values: bool
    :returns: updated dict
    :rtype: dict
    """
    for k, v in new_dict.items():
        if k in old_dict.keys():
            if isinstance(v, dict) and isinstance(old_dict[k], dict):
                old_dict[k] = update_nested_dict(
                    old_dict[k], v, extend_list_values=extend_list_values
                )
            elif (
                extend_list_values
                and isinstance(old_dict[k], list)
                and isinstance(v, list)
            ):
                old_dict[k].extend(v)
            elif v:
                old_dict[k] = v
        else:
            old_dict[k] = v
    return old_dict


def dict_items_recursive_apply(config_dict, apply_method, **apply_method_parameters):
    """Recursive apply method to dict elements

    :param config_dict: input nested dictionnary
    :type config_dict: dict
    :param apply_method: method to be applied to dict elements
    :type apply_method: :func:`apply_method`
    :param apply_method_parameters: optional parameters passed to the method
    :type apply_method_parameters: dict
    :returns: updated dict
    :rtype: dict
    """
    jsonpath_dict = copy.deepcopy(config_dict)
    for dict_k, dict_v in jsonpath_dict.items():
        if isinstance(dict_v, dict):
            jsonpath_dict[dict_k] = dict_items_recursive_apply(
                dict_v, apply_method, **apply_method_parameters
            )
        elif any(isinstance(dict_v, t) for t in (list, tuple)):
            for list_idx, list_v in enumerate(dict_v):
                if isinstance(list_v, dict):
                    jsonpath_dict[dict_k][list_idx] = dict_items_recursive_apply(
                        list_v, apply_method, **apply_method_parameters
                    )
                else:
                    jsonpath_dict[dict_k][list_idx] = apply_method(
                        dict_k, list_v, **apply_method_parameters
                    )
        else:
            jsonpath_dict[dict_k] = apply_method(
                dict_k, dict_v, **apply_method_parameters
            )

    return jsonpath_dict
