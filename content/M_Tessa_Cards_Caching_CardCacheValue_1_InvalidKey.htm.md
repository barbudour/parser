# CardCacheValue<T>.InvalidKey - метод
Создаёт объект, который содержит ошибку: переданный ключ key является
недопустимым для кэша. Свойство
[Result](P_Tessa_Cards_Caching_CardCacheValue_1_Result.htm) созданного объекта
равно [InvalidKey](T_Tessa_Cards_Caching_CardCacheResult.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardCacheValue<T> InvalidKey(
    	string key
    )
VB __Копировать
     Public Shared Function InvalidKey ( 
    	key As String
    ) As CardCacheValue(Of T)
C++ __Копировать
     public:
    static CardCacheValue<T> InvalidKey(
    	String^ key
    )
F# __Копировать
     static member InvalidKey : 
            key : string -> CardCacheValue<'T> 
#### Параметры
key [String](https://learn.microsoft.com/dotnet/api/system.string)
    Ключ, по которому было запрошено значение.
#### Возвращаемое значение
[CardCacheValue](T_Tessa_Cards_Caching_CardCacheValue_1.htm)<[T](T_Tessa_Cards_Caching_CardCacheValue_1.htm)>  
Созданное значение.
##  __См. также
#### Ссылки
[CardCacheValue<T> \- ](T_Tessa_Cards_Caching_CardCacheValue_1.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
