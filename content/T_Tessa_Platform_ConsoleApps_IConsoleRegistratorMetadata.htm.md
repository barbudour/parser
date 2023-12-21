# IConsoleRegistratorMetadata - интерфейс
Метаинформация по атрибуту
[ConsoleRegistratorAttribute](T_Tessa_Platform_ConsoleApps_ConsoleRegistratorAttribute.htm).
## __Definition
 **Пространство имён:**
[Tessa.Platform.ConsoleApps](N_Tessa_Platform_ConsoleApps.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IConsoleRegistratorMetadata : ISerializableMetadata<IConsoleRegistratorMetadata>
VB __Копировать
     Public Interface IConsoleRegistratorMetadata
    	Inherits ISerializableMetadata(Of IConsoleRegistratorMetadata)
C++ __Копировать
     public interface class IConsoleRegistratorMetadata : ISerializableMetadata<IConsoleRegistratorMetadata^>
F# __Копировать
     type IConsoleRegistratorMetadata = 
        interface
            interface ISerializableMetadata<IConsoleRegistratorMetadata>
        end
Implements
    [ISerializableMetadata](T_Tessa_Platform_Composition_ISerializableMetadata_1.htm)<IConsoleRegistratorMetadata>
##  __Свойства
[Description](P_Tessa_Platform_ConsoleApps_IConsoleRegistratorMetadata_Description.htm)|
Описание регистратора. Не используется платформой, но может предоставляться в
информативных целях.  
---|---  
[Order](P_Tessa_Platform_ConsoleApps_IConsoleRegistratorMetadata_Order.htm)|
Порядок выполнения регистратора внутри этапа
[Tessa.Extensions.IRegistratorMetadata.Order].  
[Stage](P_Tessa_Platform_ConsoleApps_IConsoleRegistratorMetadata_Stage.htm)|
Этап выполнения регистратора в цепочке регистрации.  
##  __Методы
[GetSerializable](M_Tessa_Platform_Composition_ISerializableMetadata_1_GetSerializable.htm)|
Возвращает метаинформацию, которая может быть сериализована через атрибут
[System.SerializableAttribute]. Если текущий объект уже сериализуется, то он
может вернуть себя же.  
(Унаследован от
[ISerializableMetadata<TMetadata>](T_Tessa_Platform_Composition_ISerializableMetadata_1.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Platform.ConsoleApps - пространство
имён](N_Tessa_Platform_ConsoleApps.htm)
