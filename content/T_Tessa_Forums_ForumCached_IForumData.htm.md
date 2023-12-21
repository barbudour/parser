# IForumData - интерфейс
Информация по статусу топиков у пользователя.
## __Definition
 **Пространство имён:**
[Tessa.Forums.ForumCached](N_Tessa_Forums_ForumCached.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IForumData : IStorageObjectProvider, 
    	IStorageDictionaryProvider, IStorageProvider
VB __Копировать
     Public Interface IForumData
    	Inherits IStorageObjectProvider, IStorageDictionaryProvider, IStorageProvider
C++ __Копировать
     public interface class IForumData : IStorageObjectProvider, 
    	IStorageDictionaryProvider, IStorageProvider
F# __Копировать
     type IForumData = 
        interface
            interface IStorageObjectProvider
            interface IStorageDictionaryProvider
            interface IStorageProvider
        end
Implements
    [IStorageDictionaryProvider](T_Tessa_Platform_Storage_IStorageDictionaryProvider.htm), [IStorageObjectProvider](T_Tessa_Platform_Storage_IStorageObjectProvider.htm), [IStorageProvider](T_Tessa_Platform_Storage_IStorageProvider.htm)
##  __Свойства
[ReadTopicStatusList](P_Tessa_Forums_ForumCached_IForumData_ReadTopicStatusList.htm)|
Информация по прочитанным сообщениям в топиках.  
---|---  
[TopicTypes](P_Tessa_Forums_ForumCached_IForumData_TopicTypes.htm)|  Список
всех типов топиков из таблицы FmTopicTypes.  
## __Методы
[GetStorage](M_Tessa_Platform_Storage_IStorageObjectProvider_GetStorage.htm)|
Возвращает хранилище Dictionary<string, object>, декоратором для которого
является текущий объект.  
(Унаследован от
[IStorageObjectProvider](T_Tessa_Platform_Storage_IStorageObjectProvider.htm))  
---|---  
##  __Методы расширения
[ToSerializable](M_Tessa_Platform_Storage_StorageExtensions_ToSerializable_3.htm)|
Возвращает сериализуемый объект, полученный для заданного объекта,
предоставляющего доступ к хранилищу Dictionary<string, object>.  
(Определяется
[StorageExtensions](T_Tessa_Platform_Storage_StorageExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Forums.ForumCached - пространство имён](N_Tessa_Forums_ForumCached.htm)
