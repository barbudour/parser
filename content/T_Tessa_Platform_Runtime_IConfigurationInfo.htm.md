# IConfigurationInfo - интерфейс
Информация по текущей конфигурации.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IConfigurationInfo : IStorageSerializable, 
    	ISealable
VB __Копировать
     Public Interface IConfigurationInfo
    	Inherits IStorageSerializable, ISealable
C++ __Копировать
     public interface class IConfigurationInfo : IStorageSerializable, 
    	ISealable
F# __Копировать
     type IConfigurationInfo = 
        interface
            interface IStorageSerializable
            interface ISealable
        end
Implements
    [ISealable](T_Tessa_Platform_ISealable.htm), [IStorageSerializable](T_Tessa_Platform_Storage_IStorageSerializable.htm)
##  __Свойства
[BuildDate](P_Tessa_Platform_Runtime_IConfigurationInfo_BuildDate.htm)| Дата
выпуска сборки платформы.  
---|---  
[BuildName](P_Tessa_Platform_Runtime_IConfigurationInfo_BuildName.htm)|
Версия сборки платформы в виде строки с дополнительными суффиксами, такими как
beta для бета-версий.  
[BuildVersion](P_Tessa_Platform_Runtime_IConfigurationInfo_BuildVersion.htm)|
Версия сборки платформы.  
[Description](P_Tessa_Platform_Runtime_IConfigurationInfo_Description.htm)|
Описание текущей конфигурации, может изменяться в рамках проектного решения.  
[Flags](P_Tessa_Platform_Runtime_IConfigurationInfo_Flags.htm)|  Признак того,
что конфигурация неизвестна. Значение true актуально только в том случае, если
информацию по конфигурации не удаётся получить. По умолчанию равно false.  
[Info](P_Tessa_Platform_Runtime_IConfigurationInfo_Info.htm)| Дополнительные
настройки конфигурации, устанавливаемые расширениями.  
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[IsUnknown](P_Tessa_Platform_Runtime_IConfigurationInfo_IsUnknown.htm)|
Признак того, что конфигурация неизвестна. Значение true актуально только в
том случае, если информацию по конфигурации не удаётся получить. По умолчанию
равно false.  
[Modified](P_Tessa_Platform_Runtime_IConfigurationInfo_Modified.htm)| Дата
изменения конфигурации.  
[ModifiedByID](P_Tessa_Platform_Runtime_IConfigurationInfo_ModifiedByID.htm)|
Идентификатор сотрудника, инициировавшего изменение конфигурации, или System,
если конфигурация изменялась на сервере или при прямом подключении к БД.  
[ModifiedByName](P_Tessa_Platform_Runtime_IConfigurationInfo_ModifiedByName.htm)|
Имя сотрудника, инициировавшего изменение конфигурации, или System, если
конфигурация изменялась на сервере или при прямом подключении к БД.  
[PatchList](P_Tessa_Platform_Runtime_IConfigurationInfo_PatchList.htm)| Список
установленных патчей.  
[Version](P_Tessa_Platform_Runtime_IConfigurationInfo_Version.htm)| Порядковый
номер версии конфигурации, который увеличивается с каждым изменением.  
##  __Методы
[Deserialize](M_Tessa_Platform_Storage_IStorageSerializable_Deserialize.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Унаследован от
[IStorageSerializable](T_Tessa_Platform_Storage_IStorageSerializable.htm))  
---|---  
[Seal](M_Tessa_Platform_ISealable_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[Serialize](M_Tessa_Platform_Storage_IStorageSerializable_Serialize.htm)|
Выполняет сериализацию полей объекта в заданное хранилище.  
(Унаследован от
[IStorageSerializable](T_Tessa_Platform_Storage_IStorageSerializable.htm))  
##  __Методы расширения
[ToSerializedDictionary](M_Tessa_Platform_Storage_StorageExtensions_ToSerializedDictionary.htm)|
Сериализует объект в нетипизированный словарь.  
(Определяется
[StorageExtensions](T_Tessa_Platform_Storage_StorageExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
