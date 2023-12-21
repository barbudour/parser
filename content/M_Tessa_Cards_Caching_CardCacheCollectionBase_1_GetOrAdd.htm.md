# CardCacheCollectionBase<T>.GetOrAdd - метод
Возвращает значение из кэша, или добавляет значение в кэш, возвращённое
заданной функцией при отсутствии там значения.
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected T GetOrAdd(
    	string key,
    	Func<string, T> getValueFunc
    )
VB __Копировать
     Protected Function GetOrAdd ( 
    	key As String,
    	getValueFunc As Func(Of String, T)
    ) As T
C++ __Копировать
     protected:
    T GetOrAdd(
    	String^ key, 
    	Func<String^, T>^ getValueFunc
    )
F# __Копировать
     member GetOrAdd : 
            key : string * 
            getValueFunc : Func<string, 'T> -> 'T 
#### Параметры
key [String](https://learn.microsoft.com/dotnet/api/system.string)
    Ключ, по которому требуется получить значение из кэша.
getValueFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[T](T_Tessa_Cards_Caching_CardCacheCollectionBase_1.htm)>
     Функция, получающая ключ и создающая значение. Функция используется в случае, если значение отсутствует в кэше, причём результат функции добавляется в кэш. 
#### Возвращаемое значение
[T](T_Tessa_Cards_Caching_CardCacheCollectionBase_1.htm)  
Значение, полученное из кэша или созданное заданной функцией.
##  __См. также
#### Ссылки
[CardCacheCollectionBase<T> \-
](T_Tessa_Cards_Caching_CardCacheCollectionBase_1.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
