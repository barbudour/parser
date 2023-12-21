# ConsoleRegistratorMetadata - класс
Метаинформация по атрибуту
[ConsoleRegistratorAttribute](T_Tessa_Platform_ConsoleApps_ConsoleRegistratorAttribute.htm),
представленная в сериализуемой форме.
## __Definition
 **Пространство имён:**
[Tessa.Platform.ConsoleApps](N_Tessa_Platform_ConsoleApps.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class ConsoleRegistratorMetadata : IConsoleRegistratorMetadata, 
    	ISerializableMetadata<IConsoleRegistratorMetadata>
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class ConsoleRegistratorMetadata
    	Implements IConsoleRegistratorMetadata, ISerializableMetadata(Of IConsoleRegistratorMetadata)
C++ __Копировать
    [SerializableAttribute]
    public ref class ConsoleRegistratorMetadata sealed : IConsoleRegistratorMetadata, 
    	ISerializableMetadata<IConsoleRegistratorMetadata^>
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type ConsoleRegistratorMetadata = 
        class
            interface IConsoleRegistratorMetadata
            interface ISerializableMetadata<IConsoleRegistratorMetadata>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ConsoleRegistratorMetadata
Implements
    [ISerializableMetadata](T_Tessa_Platform_Composition_ISerializableMetadata_1.htm)<[IConsoleRegistratorMetadata](T_Tessa_Platform_ConsoleApps_IConsoleRegistratorMetadata.htm)>, [IConsoleRegistratorMetadata](T_Tessa_Platform_ConsoleApps_IConsoleRegistratorMetadata.htm)
##  __Конструкторы
[ConsoleRegistratorMetadata](M_Tessa_Platform_ConsoleApps_ConsoleRegistratorMetadata__ctor.htm)|
Создаёт экземпляр класса с указанием объекта, по свойствам которого создаётся
текущий объект.  
---|---  
## __Свойства
[Description](P_Tessa_Platform_ConsoleApps_ConsoleRegistratorMetadata_Description.htm)|
Описание регистратора. Не используется платформой, но может предоставляться в
информативных целях.  
---|---  
[Order](P_Tessa_Platform_ConsoleApps_ConsoleRegistratorMetadata_Order.htm)|
Порядок выполнения регистратора внутри этапа
[Tessa.Extensions.IRegistratorMetadata.Order].  
[Stage](P_Tessa_Platform_ConsoleApps_ConsoleRegistratorMetadata_Stage.htm)|
Этап выполнения регистратора в цепочке регистрации.  
##  __Методы
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
[GetSerializable](M_Tessa_Platform_ConsoleApps_ConsoleRegistratorMetadata_GetSerializable.htm)|
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
