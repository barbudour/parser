# ExampleAttribute - класс
Specifies an example for a command.
## __Definition
 **Пространство имён:**
[Tessa.Platform.CommandLine](N_Tessa_Platform_CommandLine.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [AttributeUsageAttribute(AttributeTargets.Method, AllowMultiple = true)]
    public class ExampleAttribute : Attribute
VB __Копировать
    <AttributeUsageAttribute(AttributeTargets.Method, AllowMultiple := true)>
    Public Class ExampleAttribute
    	Inherits Attribute
C++ __Копировать
    [AttributeUsageAttribute(AttributeTargets::Method, AllowMultiple = true)]
    public ref class ExampleAttribute : public Attribute
F# __Копировать
     [<AttributeUsageAttribute(AttributeTargets.Method, AllowMultiple = true)>]
    type ExampleAttribute = 
        class
            inherit Attribute
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute) __ ExampleAttribute
##  __Конструкторы
[ExampleAttribute(String)](M_Tessa_Platform_CommandLine_ExampleAttribute__ctor.htm)|
Initializes a new instance of the ExampleAttribute class using the specified
example.  
---|---  
[ExampleAttribute(String,
Char)](M_Tessa_Platform_CommandLine_ExampleAttribute__ctor_1.htm)|
Инициализирует новый экземпляр класса ExampleAttribute  
[ExampleAttribute(String,
String)](M_Tessa_Platform_CommandLine_ExampleAttribute__ctor_3.htm)|
Initializes a new instance of the ExampleAttribute class using the specified
example and description.  
[ExampleAttribute(String, Char,
String)](M_Tessa_Platform_CommandLine_ExampleAttribute__ctor_2.htm)|
Инициализирует новый экземпляр класса ExampleAttribute  
##  __Свойства
[Description](P_Tessa_Platform_CommandLine_ExampleAttribute_Description.htm)|
Gets the description stored in this attribute.  
---|---  
[DescriptionValue](P_Tessa_Platform_CommandLine_ExampleAttribute_DescriptionValue.htm)|
Gets or sets the string stored as the description.  
[Example](P_Tessa_Platform_CommandLine_ExampleAttribute_Example.htm)|  Gets
the example stored in this attribute.  
[NamePrefix](P_Tessa_Platform_CommandLine_ExampleAttribute_NamePrefix.htm)|  
[TypeId](https://learn.microsoft.com/dotnet/api/system.attribute.typeid#system-
attribute-typeid)| When implemented in a derived class, gets a unique
identifier for this
[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute).  
(Унаследован от
[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute))  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.attribute.equals#system-
attribute-equals\(system-object\))| Returns a value that indicates whether
this instance is equal to a specified object.  
(Унаследован от
[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.attribute.gethashcode#system-
attribute-gethashcode)| Returns the hash code for this instance.  
(Унаследован от
[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IsDefaultAttribute](https://learn.microsoft.com/dotnet/api/system.attribute.isdefaultattribute#system-
attribute-isdefaultattribute)| When overridden in a derived class, indicates
whether the value of this instance is the default value for the derived class.  
(Унаследован от
[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute))  
[Match](https://learn.microsoft.com/dotnet/api/system.attribute.match#system-
attribute-match\(system-object\))| When overridden in a derived class, returns
a value that indicates whether this instance equals a specified object.  
(Унаследован от
[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.CommandLine - пространство
имён](N_Tessa_Platform_CommandLine.htm)
