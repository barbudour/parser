# ICardFileSourceOverrideSettings - интерфейс
Настройки, переопределяющие местоположение контента файла.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardFileSourceOverrideSettings : IStorageSerializable, 
    	ISealable
VB __Копировать
     Public Interface ICardFileSourceOverrideSettings
    	Inherits IStorageSerializable, ISealable
C++ __Копировать
     public interface class ICardFileSourceOverrideSettings : IStorageSerializable, 
    	ISealable
F# __Копировать
     type ICardFileSourceOverrideSettings = 
        interface
            interface IStorageSerializable
            interface ISealable
        end
Implements
    [ISealable](T_Tessa_Platform_ISealable.htm), [IStorageSerializable](T_Tessa_Platform_Storage_IStorageSerializable.htm)
##  __Свойства
[FileSourceOverrides](P_Tessa_Cards_ICardFileSourceOverrideSettings_FileSourceOverrides.htm)|
Список объектов
[ICardFileSourceOverride](T_Tessa_Cards_ICardFileSourceOverride.htm).  
---|---  
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
