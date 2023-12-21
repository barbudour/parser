# ISerializableMetadata<TMetadata> \- интерфейс
Экспортируемые из сборок метаданные, поддерживающие сериализацию. Используется
для сериализации метаданных.
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISerializableMetadata<out TMetadata>
VB __Копировать
     Public Interface ISerializableMetadata(Of Out TMetadata)
C++ __Копировать
    generic<typename TMetadata>
    public interface class ISerializableMetadata
F# __Копировать
     type ISerializableMetadata<'TMetadata> = interface end
#### Параметры типа
TMetadata
    Тип экспортируемых метаданных.
##  __Методы
[GetSerializable](M_Chronos_Contracts_ISerializableMetadata_1_GetSerializable.htm)|
Возвращает метаинформацию, которая может быть сериализована через атрибут
[System.SerializableAttribute]. Если текущий объект уже сериализуется, то он
может вернуть себя же.  
---|---  
## __См. также
#### Ссылки
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
