# ISerializableMetadata<TMetadata> \- интерфейс
Экспортируемые из сборок метаданные, поддерживающие сериализацию. Используется
для сериализации.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Composition](N_Tessa_Platform_Composition.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
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
[GetSerializable](M_Tessa_Platform_Composition_ISerializableMetadata_1_GetSerializable.htm)|
Возвращает метаинформацию, которая может быть сериализована через атрибут
[System.SerializableAttribute]. Если текущий объект уже сериализуется, то он
может вернуть себя же.  
---|---  
## __См. также
#### Ссылки
[Tessa.Platform.Composition - пространство
имён](N_Tessa_Platform_Composition.htm)
