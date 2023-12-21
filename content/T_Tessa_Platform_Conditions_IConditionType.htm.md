# IConditionType - интерфейс
Объект, содержащий информацию о типе условия.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Conditions](N_Tessa_Platform_Conditions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IConditionType : IStorageSerializable
VB __Копировать
     Public Interface IConditionType
    	Inherits IStorageSerializable
C++ __Копировать
     public interface class IConditionType : IStorageSerializable
F# __Копировать
     type IConditionType = 
        interface
            interface IStorageSerializable
        end
Implements
    [IStorageSerializable](T_Tessa_Platform_Storage_IStorageSerializable.htm)
##  __Свойства
[ConditionText](P_Tessa_Platform_Conditions_IConditionType_ConditionText.htm)|
Шаблон описания условия.  
---|---  
[ID](P_Tessa_Platform_Conditions_IConditionType_ID.htm)|  Идентификатор типа
условия.  
[Name](P_Tessa_Platform_Conditions_IConditionType_Name.htm)|  Имя типа
условия.  
[SettingsTypeID](P_Tessa_Platform_Conditions_IConditionType_SettingsTypeID.htm)|
Идентификатор типа карточки с настройками.  
[UsePlaces](P_Tessa_Platform_Conditions_IConditionType_UsePlaces.htm)|  Список
мест использования типа условия.  
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
[Tessa.Platform.Conditions - пространство
имён](N_Tessa_Platform_Conditions.htm)
