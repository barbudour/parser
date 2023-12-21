# CollectionConverter - класс
##  __Definition
 **Пространство имён:**
[Tessa.Platform.Collections](N_Tessa_Platform_Collections.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class CollectionConverter : TypeConverter
VB __Копировать
     Public Class CollectionConverter
    	Inherits TypeConverter
C++ __Копировать
     public ref class CollectionConverter : public TypeConverter
F# __Копировать
     type CollectionConverter = 
        class
            inherit TypeConverter
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter) __ CollectionConverter
##  __Конструкторы
[CollectionConverter(Type)](M_Tessa_Platform_Collections_CollectionConverter__ctor.htm)|
Инициализирует новый экземпляр класса CollectionConverter  
---|---  
[CollectionConverter(Type,
Type)](M_Tessa_Platform_Collections_CollectionConverter__ctor_1.htm)|
Инициализирует новый экземпляр класса CollectionConverter  
##  __Методы
[CanConvertFrom(Type)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.canconvertfrom#system-
componentmodel-typeconverter-canconvertfrom\(system-type\))| Returns whether
this converter can convert an object of the given type to the type of this
converter.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
---|---  
[CanConvertFrom(ITypeDescriptorContext,
Type)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.canconvertfrom#system-
componentmodel-typeconverter-canconvertfrom\(system-componentmodel-
itypedescriptorcontext-system-type\))| Returns whether this converter can
convert an object of the given type to the type of this converter, using the
specified context.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[CanConvertFrom(ITypeDescriptorContext,
Type)](M_Tessa_Platform_Collections_CollectionConverter_CanConvertFrom.htm)|  
[CanConvertTo(Type)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.canconvertto#system-
componentmodel-typeconverter-canconvertto\(system-type\))| Returns whether
this converter can convert the object to the specified type.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[CanConvertTo(ITypeDescriptorContext,
Type)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.canconvertto#system-
componentmodel-typeconverter-canconvertto\(system-componentmodel-
itypedescriptorcontext-system-type\))| Returns whether this converter can
convert the object to the specified type, using the specified context.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[ConvertFrom(Object)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.convertfrom#system-
componentmodel-typeconverter-convertfrom\(system-object\))| Converts the given
value to the type of this converter.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[ConvertFrom(ITypeDescriptorContext, CultureInfo,
Object)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.convertfrom#system-
componentmodel-typeconverter-convertfrom\(system-componentmodel-
itypedescriptorcontext-system-globalization-cultureinfo-system-object\))|
Converts the given object to the type of this converter, using the specified
context and culture information.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[ConvertFrom(ITypeDescriptorContext, CultureInfo,
Object)](M_Tessa_Platform_Collections_CollectionConverter_ConvertFrom.htm)|  
[ConvertFromInvariantString(String)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.convertfrominvariantstring#system-
componentmodel-typeconverter-convertfrominvariantstring\(system-string\))|
Converts the given string to the type of this converter, using the invariant
culture.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[ConvertFromInvariantString(ITypeDescriptorContext,
String)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.convertfrominvariantstring#system-
componentmodel-typeconverter-convertfrominvariantstring\(system-
componentmodel-itypedescriptorcontext-system-string\))| Converts the given
string to the type of this converter, using the invariant culture and the
specified context.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[ConvertFromString(String)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.convertfromstring#system-
componentmodel-typeconverter-convertfromstring\(system-string\))| Converts the
specified text to an object.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[ConvertFromString(ITypeDescriptorContext,
String)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.convertfromstring#system-
componentmodel-typeconverter-convertfromstring\(system-componentmodel-
itypedescriptorcontext-system-string\))| Converts the given text to an object,
using the specified context.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[ConvertFromString(ITypeDescriptorContext, CultureInfo,
String)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.convertfromstring#system-
componentmodel-typeconverter-convertfromstring\(system-componentmodel-
itypedescriptorcontext-system-globalization-cultureinfo-system-string\))|
Converts the given text to an object, using the specified context and culture
information.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[ConvertTo(Object,
Type)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.convertto#system-
componentmodel-typeconverter-convertto\(system-object-system-type\))| Converts
the given value object to the specified type, using the arguments.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[ConvertTo(ITypeDescriptorContext, CultureInfo, Object,
Type)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.convertto#system-
componentmodel-typeconverter-convertto\(system-componentmodel-
itypedescriptorcontext-system-globalization-cultureinfo-system-object-system-
type\))| Converts the given value object to the specified type, using the
specified context and culture information.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[ConvertToInvariantString(Object)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.converttoinvariantstring#system-
componentmodel-typeconverter-converttoinvariantstring\(system-object\))|
Converts the specified value to a culture-invariant string representation.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[ConvertToInvariantString(ITypeDescriptorContext,
Object)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.converttoinvariantstring#system-
componentmodel-typeconverter-converttoinvariantstring\(system-componentmodel-
itypedescriptorcontext-system-object\))| Converts the specified value to a
culture-invariant string representation, using the specified context.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[ConvertToString(Object)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.converttostring#system-
componentmodel-typeconverter-converttostring\(system-object\))| Converts the
specified value to a string representation.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[ConvertToString(ITypeDescriptorContext,
Object)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.converttostring#system-
componentmodel-typeconverter-converttostring\(system-componentmodel-
itypedescriptorcontext-system-object\))| Converts the given value to a string
representation, using the given context.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[ConvertToString(ITypeDescriptorContext, CultureInfo,
Object)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.converttostring#system-
componentmodel-typeconverter-converttostring\(system-componentmodel-
itypedescriptorcontext-system-globalization-cultureinfo-system-object\))|
Converts the given value to a string representation, using the specified
context and culture information.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[CreateInstance(IDictionary)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.createinstance#system-
componentmodel-typeconverter-createinstance\(system-collections-
idictionary\))| Re-creates an
[Object](https://learn.microsoft.com/dotnet/api/system.object) given a set of
property values for the object.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[CreateInstance(ITypeDescriptorContext,
IDictionary)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.createinstance#system-
componentmodel-typeconverter-createinstance\(system-componentmodel-
itypedescriptorcontext-system-collections-idictionary\))| Creates an instance
of the type that this
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter)
is associated with, using the specified context, given a set of property
values for the object.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetConvertFromException](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.getconvertfromexception#system-
componentmodel-typeconverter-getconvertfromexception\(system-object\))|
Returns an exception to throw when a conversion cannot be performed.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[GetConvertToException](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.getconverttoexception#system-
componentmodel-typeconverter-getconverttoexception\(system-object-system-
type\))| Returns an exception to throw when a conversion cannot be performed.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[GetCreateInstanceSupported()](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.getcreateinstancesupported#system-
componentmodel-typeconverter-getcreateinstancesupported)| Returns whether
changing a value on this object requires a call to the
[CreateInstance(IDictionary)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.createinstance#system-
componentmodel-typeconverter-createinstance\(system-collections-idictionary\))
method to create a new value.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[GetCreateInstanceSupported(ITypeDescriptorContext)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.getcreateinstancesupported#system-
componentmodel-typeconverter-getcreateinstancesupported\(system-
componentmodel-itypedescriptorcontext\))| Returns whether changing a value on
this object requires a call to
[CreateInstance(IDictionary)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.createinstance#system-
componentmodel-typeconverter-createinstance\(system-collections-idictionary\))
to create a new value, using the specified context.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetProperties(Object)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.getproperties#system-
componentmodel-typeconverter-getproperties\(system-object\))| Returns a
collection of properties for the type of array specified by the value
parameter.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[GetProperties(ITypeDescriptorContext,
Object)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.getproperties#system-
componentmodel-typeconverter-getproperties\(system-componentmodel-
itypedescriptorcontext-system-object\))| Returns a collection of properties
for the type of array specified by the value parameter, using the specified
context.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[GetProperties(ITypeDescriptorContext, Object,
Attribute[])](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.getproperties#system-
componentmodel-typeconverter-getproperties\(system-componentmodel-
itypedescriptorcontext-system-object-system-attribute\(\)\))| Returns a
collection of properties for the type of array specified by the value
parameter, using the specified context and attributes.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[GetPropertiesSupported()](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.getpropertiessupported#system-
componentmodel-typeconverter-getpropertiessupported)| Returns whether this
object supports properties.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[GetPropertiesSupported(ITypeDescriptorContext)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.getpropertiessupported#system-
componentmodel-typeconverter-getpropertiessupported\(system-componentmodel-
itypedescriptorcontext\))| Returns whether this object supports properties,
using the specified context.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[GetStandardValues()](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.getstandardvalues#system-
componentmodel-typeconverter-getstandardvalues)| Returns a collection of
standard values from the default context for the data type this type converter
is designed for.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[GetStandardValues(ITypeDescriptorContext)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.getstandardvalues#system-
componentmodel-typeconverter-getstandardvalues\(system-componentmodel-
itypedescriptorcontext\))| Returns a collection of standard values for the
data type this type converter is designed for when provided with a format
context.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[GetStandardValuesExclusive()](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.getstandardvaluesexclusive#system-
componentmodel-typeconverter-getstandardvaluesexclusive)| Returns whether the
collection of standard values returned from
[GetStandardValues()](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.getstandardvalues#system-
componentmodel-typeconverter-getstandardvalues) is an exclusive list.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[GetStandardValuesExclusive(ITypeDescriptorContext)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.getstandardvaluesexclusive#system-
componentmodel-typeconverter-getstandardvaluesexclusive\(system-
componentmodel-itypedescriptorcontext\))| Returns whether the collection of
standard values returned from
[GetStandardValues()](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.getstandardvalues#system-
componentmodel-typeconverter-getstandardvalues) is an exclusive list of
possible values, using the specified context.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[GetStandardValuesSupported()](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.getstandardvaluessupported#system-
componentmodel-typeconverter-getstandardvaluessupported)| Returns whether this
object supports a standard set of values that can be picked from a list.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[GetStandardValuesSupported(ITypeDescriptorContext)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.getstandardvaluessupported#system-
componentmodel-typeconverter-getstandardvaluessupported\(system-
componentmodel-itypedescriptorcontext\))| Returns whether this object supports
a standard set of values that can be picked from a list, using the specified
context.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IsValid(Object)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.isvalid#system-
componentmodel-typeconverter-isvalid\(system-object\))| Returns whether the
given value object is valid for this type.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[IsValid(ITypeDescriptorContext,
Object)](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.isvalid#system-
componentmodel-typeconverter-isvalid\(system-componentmodel-
itypedescriptorcontext-system-object\))| Returns whether the given value
object is valid for this type and for the specified context.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[SortProperties](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter.sortproperties#system-
componentmodel-typeconverter-sortproperties\(system-componentmodel-
propertydescriptorcollection-system-string\(\)\))| Sorts a collection of
properties.  
(Унаследован от
[TypeConverter](https://learn.microsoft.com/dotnet/api/system.componentmodel.typeconverter))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __См. также
#### Ссылки
[Tessa.Platform.Collections - пространство
имён](N_Tessa_Platform_Collections.htm)
