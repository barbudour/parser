# ConsoleScriptAttribute - класс
Атрибут, указывающий метаданные объекта класса скрипта, на основании которых
будет выполняться выполнение скриптов.
## __Definition
 **Пространство имён:**
[Tessa.Platform.ConsoleApps](N_Tessa_Platform_ConsoleApps.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [AttributeUsageAttribute(AttributeTargets.Class, Inherited = false)]
    public sealed class ConsoleScriptAttribute : Attribute, 
    	IConsoleScriptMetadata, ISerializableMetadata<IConsoleScriptMetadata>
VB __Копировать
    <AttributeUsageAttribute(AttributeTargets.Class, Inherited := false)>
    Public NotInheritable Class ConsoleScriptAttribute
    	Inherits Attribute
    	Implements IConsoleScriptMetadata, ISerializableMetadata(Of IConsoleScriptMetadata)
C++ __Копировать
    [AttributeUsageAttribute(AttributeTargets::Class, Inherited = false)]
    public ref class ConsoleScriptAttribute sealed : public Attribute, 
    	IConsoleScriptMetadata, ISerializableMetadata<IConsoleScriptMetadata^>
F# __Копировать
     [<SealedAttribute>]
    [<AttributeUsageAttribute(AttributeTargets.Class, Inherited = false)>]
    type ConsoleScriptAttribute = 
        class
            inherit Attribute
            interface IConsoleScriptMetadata
            interface ISerializableMetadata<IConsoleScriptMetadata>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute) __ ConsoleScriptAttribute
Implements
    [ISerializableMetadata](T_Tessa_Platform_Composition_ISerializableMetadata_1.htm)<[IConsoleScriptMetadata](T_Tessa_Platform_ConsoleApps_IConsoleScriptMetadata.htm)>, [IConsoleScriptMetadata](T_Tessa_Platform_ConsoleApps_IConsoleScriptMetadata.htm)
##  __Заметки
Атрибут должен использоваться на классе, реализующем интерфейс
[IConsoleScript](T_Tessa_Platform_ConsoleApps_IConsoleScript.htm).
## __Конструкторы
[ConsoleScriptAttribute](M_Tessa_Platform_ConsoleApps_ConsoleScriptAttribute__ctor.htm)|
Создаёт экземпляр класса с указанием имени скрипта.  
---|---  
## __Свойства
[Name](P_Tessa_Platform_ConsoleApps_ConsoleScriptAttribute_Name.htm)|  
---|---  
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
[GetSerializable](M_Tessa_Platform_ConsoleApps_ConsoleScriptAttribute_GetSerializable.htm)|
Возвращает метаинформацию, которая может быть сериализована через атрибут
[System.SerializableAttribute]. Если текущий объект уже сериализуется, то он
может вернуть себя же.  
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
[Tessa.Platform.ConsoleApps - пространство
имён](N_Tessa_Platform_ConsoleApps.htm)
