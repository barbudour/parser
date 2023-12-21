# CardCacheCollectionBase<T>.TryGetValue - метод
Возвращает значение из кэша value, если оно присутствует, или false, если
значения нет в кэше.
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected bool TryGetValue(
    	string key,
    	out T value
    )
VB __Копировать
     Protected Function TryGetValue ( 
    	key As String,
    	<OutAttribute> ByRef value As T
    ) As Boolean
C++ __Копировать
     protected:
    bool TryGetValue(
    	String^ key, 
    	[OutAttribute] T% value
    )
F# __Копировать
     member TryGetValue : 
            key : string * 
            value : 'T byref -> bool 
#### Параметры
key [String](https://learn.microsoft.com/dotnet/api/system.string)
    Ключ, по которому требуется получить значение из кэша.
value [T](T_Tessa_Cards_Caching_CardCacheCollectionBase_1.htm)
    Возвращённое из кэша значение. Актуально, если метод вернул true.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Значение, полученное из кэша или созданное заданной функцией.
##  __См. также
#### Ссылки
[CardCacheCollectionBase<T> \-
](T_Tessa_Cards_Caching_CardCacheCollectionBase_1.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
