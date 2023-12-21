# ITessaPatchInfo - интерфейс
Информация по патчу, установленному на сервер TESSA.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ITessaPatchInfo : ISealable, 
    	IStorageSerializable
VB __Копировать
     Public Interface ITessaPatchInfo
    	Inherits ISealable, IStorageSerializable
C++ __Копировать
     public interface class ITessaPatchInfo : ISealable, 
    	IStorageSerializable
F# __Копировать
     type ITessaPatchInfo = 
        interface
            interface ISealable
            interface IStorageSerializable
        end
Implements
    [ISealable](T_Tessa_Platform_ISealable.htm), [IStorageSerializable](T_Tessa_Platform_Storage_IStorageSerializable.htm)
##  __Свойства
[Date](P_Tessa_Platform_ITessaPatchInfo_Date.htm)| Дата выпуска патча.  
---|---  
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[Name](P_Tessa_Platform_ITessaPatchInfo_Name.htm)| Название патча.  
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
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
