# ICardMergeOptions - интерфейс
Представляет параметры слияния для объектов Card
## __Definition
 **Пространство имён:** [Tessa.Cards.SmartMerge](N_Tessa_Cards_SmartMerge.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardMergeOptions : IMergeOptions, 
    	IStorageSerializable
VB __Копировать
     Public Interface ICardMergeOptions
    	Inherits IMergeOptions, IStorageSerializable
C++ __Копировать
     public interface class ICardMergeOptions : IMergeOptions, 
    	IStorageSerializable
F# __Копировать
     type ICardMergeOptions = 
        interface
            interface IMergeOptions
            interface IStorageSerializable
        end
Implements
    [IStorageSerializable](T_Tessa_Platform_Storage_IStorageSerializable.htm), [IMergeOptions](T_Tessa_SmartMerge_IMergeOptions.htm)
##  __Свойства
[FileSettings](P_Tessa_Cards_SmartMerge_ICardMergeOptions_FileSettings.htm)|
Параметры слияния для прикрепленных файлов  
---|---  
[IgnoreDuplicateRows](P_Tessa_SmartMerge_IMergeOptions_IgnoreDuplicateRows.htm)|
Отвечает за логику в случае более одного совпадения по ключевым полям на одном
"тир-уровне", true - игнорировать дубликаты, false - логика зависит от
реализации (например инсертить дубликаты с занесением как Warning в
ValidationResult)  
(Унаследован от [IMergeOptions](T_Tessa_SmartMerge_IMergeOptions.htm))  
[SectionsSettings](P_Tessa_Cards_SmartMerge_ICardMergeOptions_SectionsSettings.htm)|
Список параметров слияния для секций  
[SkipIfCardExists](P_Tessa_Cards_SmartMerge_ICardMergeOptions_SkipIfCardExists.htm)|
Пропустить импорт, если карточка уже существует в БД.  
## __Методы
[Deserialize](M_Tessa_Platform_Storage_IStorageSerializable_Deserialize.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Унаследован от
[IStorageSerializable](T_Tessa_Platform_Storage_IStorageSerializable.htm))  
---|---  
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
[Tessa.Cards.SmartMerge - пространство имён](N_Tessa_Cards_SmartMerge.htm)
