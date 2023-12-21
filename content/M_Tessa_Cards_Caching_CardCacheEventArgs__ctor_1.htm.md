# CardCacheEventArgs(CardCacheInvalidationType, String) - конструктор
Создаёт экземпляр класса с указанием параметров операции по сбросу кэша.
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardCacheEventArgs(
    	CardCacheInvalidationType invalidationType,
    	string key = null
    )
VB __Копировать
     Public Sub New ( 
    	invalidationType As CardCacheInvalidationType,
    	Optional key As String = Nothing
    )
C++ __Копировать
     public:
    CardCacheEventArgs(
    	CardCacheInvalidationType invalidationType, 
    	String^ key = nullptr
    )
F# __Копировать
     new : 
            invalidationType : CardCacheInvalidationType * 
            ?key : string 
    (* Defaults:
            let _key = defaultArg key null
    *)
    -> CardCacheEventArgs
#### Параметры
invalidationType
[CardCacheInvalidationType](T_Tessa_Cards_Caching_CardCacheInvalidationType.htm)
    Тип операции по сбросу кэша.
key [String](https://learn.microsoft.com/dotnet/api/system.string) (Optional)
     Ключ, для которого выполняется сброс кэша, или null, если ключ не требуется. 
## __См. также
#### Ссылки
[CardCacheEventArgs - ](T_Tessa_Cards_Caching_CardCacheEventArgs.htm)
[CardCacheEventArgs -
перегрузка](Overload_Tessa_Cards_Caching_CardCacheEventArgs__ctor.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
