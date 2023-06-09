# -*- coding: utf-8 -*-

"""
whatsappcloudapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from whatsappcloudapi.api_helper import APIHelper


class Name(object):

    """Implementation of the 'Name' model.

    TODO: type model description here.

    Attributes:
        formatted_name (string): Full name, as it normally appears.
        first_name (string): TODO: type description here.
        last_name (string): TODO: type description here.
        middle_name (string): TODO: type description here.
        suffix (string): TODO: type description here.
        prefix (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "formatted_name": 'formatted_name',
        "first_name": 'first_name',
        "last_name": 'last_name',
        "middle_name": 'middle_name',
        "suffix": 'suffix',
        "prefix": 'prefix'
    }

    _optionals = [
        'first_name',
        'last_name',
        'middle_name',
        'suffix',
        'prefix',
    ]

    def __init__(self,
                 formatted_name=None,
                 first_name=APIHelper.SKIP,
                 last_name=APIHelper.SKIP,
                 middle_name=APIHelper.SKIP,
                 suffix=APIHelper.SKIP,
                 prefix=APIHelper.SKIP):
        """Constructor for the Name class"""

        # Initialize members of the class
        self.formatted_name = formatted_name 
        if first_name is not APIHelper.SKIP:
            self.first_name = first_name 
        if last_name is not APIHelper.SKIP:
            self.last_name = last_name 
        if middle_name is not APIHelper.SKIP:
            self.middle_name = middle_name 
        if suffix is not APIHelper.SKIP:
            self.suffix = suffix 
        if prefix is not APIHelper.SKIP:
            self.prefix = prefix 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        formatted_name = dictionary.get("formatted_name") if dictionary.get("formatted_name") else None
        first_name = dictionary.get("first_name") if dictionary.get("first_name") else APIHelper.SKIP
        last_name = dictionary.get("last_name") if dictionary.get("last_name") else APIHelper.SKIP
        middle_name = dictionary.get("middle_name") if dictionary.get("middle_name") else APIHelper.SKIP
        suffix = dictionary.get("suffix") if dictionary.get("suffix") else APIHelper.SKIP
        prefix = dictionary.get("prefix") if dictionary.get("prefix") else APIHelper.SKIP
        # Return an object of this model
        return cls(formatted_name,
                   first_name,
                   last_name,
                   middle_name,
                   suffix,
                   prefix)
