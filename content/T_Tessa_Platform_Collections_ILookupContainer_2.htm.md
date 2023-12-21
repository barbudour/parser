# ILookupContainer<TKey, TValue> \- интерфейс
Контейнер для значений, доступных по неуникальным ключам. Интерфейс позволяет
получать и удалять значения, но не добавлять их.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Collections](N_Tessa_Platform_Collections.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ILookupContainer<in TKey, TValue>
    where TValue : class
VB __Копировать
     Public Interface ILookupContainer(Of In TKey, TValue As Class)
C++ __Копировать
    generic<typename TKey, typename TValue>
    where TValue : ref class
    public interface class ILookupContainer
F# __Копировать
     type ILookupContainer<'TKey, 'TValue when 'TValue : not struct> = interface end
#### Параметры типа
TKey
    Тип ключа, по которому могут быть найдены значения.
TValue
    Ссылочный тип значения.
##  __Свойства
[Item](P_Tessa_Platform_Collections_ILookupContainer_2_Item.htm)|  Получает
одно из значений, доступных по заданному ключу, которое гарантированно не
равно null. При отсутствии таких значений выбрасывает исключение
[System.Collections.Generic.KeyNotFoundException].  
---|---  
## __Методы
[Contains](M_Tessa_Platform_Collections_ILookupContainer_2_Contains.htm)|
Возвращает признак того, что контейнер содержит хотя бы одно значение по
заданному ключу.  
---|---  
[GetAll](M_Tessa_Platform_Collections_ILookupContainer_2_GetAll.htm)|
Возвращает все значения, доступные по заданному ключу. Если таких значений
нет, то возвращается пустая коллекция.  
[Remove](M_Tessa_Platform_Collections_ILookupContainer_2_Remove.htm)|  Удаляет
одно из значений, содержащихся в контейнере по заданному ключу. Возвращает
признак того, что одно из значений было удалено.  
[RemoveAll](M_Tessa_Platform_Collections_ILookupContainer_2_RemoveAll.htm)|
Удаляет все значения, содержащиеся в контейнере по заданному ключу. Возвращает
признак того, что хотя бы одно из значений было удалено.  
[TryGet](M_Tessa_Platform_Collections_ILookupContainer_2_TryGet.htm)|
Возвращает одно из значений по заданному ключу или null, если контейнер не
содержит значений.  
## __См. также
#### Ссылки
[Tessa.Platform.Collections - пространство
имён](N_Tessa_Platform_Collections.htm)
