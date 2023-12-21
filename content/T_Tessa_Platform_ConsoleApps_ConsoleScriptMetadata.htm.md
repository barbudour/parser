# ConsoleScriptMetadata - класс
Метаинформация по атрибуту
[ConsoleScriptAttribute](T_Tessa_Platform_ConsoleApps_ConsoleScriptAttribute.htm),
представленная в сериализуемой форме.
## __Definition
 **Пространство имён:**
[Tessa.Platform.ConsoleApps](N_Tessa_Platform_ConsoleApps.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class ConsoleScriptMetadata : IConsoleScriptMetadata, 
    	ISerializableMetadata<IConsoleScriptMetadata>
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class ConsoleScriptMetadata
    	Implements IConsoleScriptMetadata, ISerializableMetadata(Of IConsoleScriptMetadata)
C++ __Копировать
    [SerializableAttribute]
    public ref class ConsoleScriptMetadata sealed : IConsoleScriptMetadata, 
    	ISerializableMetadata<IConsoleScriptMetadata^>
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type ConsoleScriptMetadata = 
        class
            interface IConsoleScriptMetadata
            interface ISerializableMetadata<IConsoleScriptMetadata>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ConsoleScriptMetadata
Implements
    [ISerializableMetadata](T_Tessa_Platform_Composition_ISerializableMetadata_1.htm)<[IConsoleScriptMetadata](T_Tessa_Platform_ConsoleApps_IConsoleScriptMetadata.htm)>, [IConsoleScriptMetadata](T_Tessa_Platform_ConsoleApps_IConsoleScriptMetadata.htm)
##  __Конструкторы
[ConsoleScriptMetadata](M_Tessa_Platform_ConsoleApps_ConsoleScriptMetadata__ctor.htm)|
Создаёт экземпляр класса с указанием объекта, по свойствам которого создаётся
текущий объект.  
---|---  
## __Свойства
[Name](P_Tessa_Platform_ConsoleApps_ConsoleScriptMetadata_Name.htm)|  Имя
скрипта, которое указывается в параметрах консольной команды для запуска
скрипта. Должно быть уникальным среди всех сборок расширений, подключённых к
консольной утилите. По умолчанию (если указаны null или пустая строка)
соотносится с полным именем типа для класса, к которому применён атрибут
[ConsoleScriptAttribute](T_Tessa_Platform_ConsoleApps_ConsoleScriptAttribute.htm).  
---|---  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetSerializable](M_Tessa_Platform_ConsoleApps_ConsoleScriptMetadata_GetSerializable.htm)|
Возвращает метаинформацию, которая может быть сериализована через атрибут
[System.SerializableAttribute]. Если текущий объект уже сериализуется, то он
может вернуть себя же.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
