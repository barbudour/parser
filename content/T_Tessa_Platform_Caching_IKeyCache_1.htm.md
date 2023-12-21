# IKeyCache<T> \- интерфейс
Кэш, осуществляющий перевод строго типизированных ключей в строки и наоборот.
## __Definition
 **Пространство имён:** [Tessa.Platform.Caching](N_Tessa_Platform_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKeyCache<T>
VB __Копировать
     Public Interface IKeyCache(Of T)
C++ __Копировать
    generic<typename T>
    public interface class IKeyCache
F# __Копировать
     type IKeyCache<'T> = interface end
#### Параметры типа
T
    Тип строго типизированного ключа.
##  __Свойства
[Capacity](P_Tessa_Platform_Caching_IKeyCache_1_Capacity.htm)|  Максимальное
количество записей в кэше или 0, если количество записей не ограничено.  
---|---  
## __Методы
[GetStringKey](M_Tessa_Platform_Caching_IKeyCache_1_GetStringKey.htm)|
Возвращает строковый ключ по строго типизированному с указанием функции
преобразования ключей.  
---|---  
[GetTypedKey](M_Tessa_Platform_Caching_IKeyCache_1_GetTypedKey.htm)|
Возвращает строго типизированный ключ по строковому с указанием функции
преобразования ключей.  
## __См. также
#### Ссылки
[Tessa.Platform.Caching - пространство имён](N_Tessa_Platform_Caching.htm)
