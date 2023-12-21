# CardSatelliteHelper.RemoveSatelliteFromList - метод
Удаляет из списка карточек-сателлитов, если он существовал в пакете основной
карточки, сателлиты указанного типа. Удаляет пустой список из структуры.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void RemoveSatelliteFromList(
    	Card mainCard,
    	string satelliteKey,
    	Guid satelliteCardTypeID,
    	bool isNot = false
    )
VB __Копировать
     Public Shared Sub RemoveSatelliteFromList ( 
    	mainCard As Card,
    	satelliteKey As String,
    	satelliteCardTypeID As Guid,
    	Optional isNot As Boolean = false
    )
C++ __Копировать
     public:
    static void RemoveSatelliteFromList(
    	Card^ mainCard, 
    	String^ satelliteKey, 
    	Guid satelliteCardTypeID, 
    	bool isNot = false
    )
F# __Копировать
     static member RemoveSatelliteFromList : 
            mainCard : Card * 
            satelliteKey : string * 
            satelliteCardTypeID : Guid * 
            ?isNot : bool 
    (* Defaults:
            let _isNot = defaultArg isNot false
    *)
    -> unit 
#### Параметры
mainCard [Card](T_Tessa_Cards_Card.htm)
    Пакет основной карточки, в которой может содержаться список карточек-сателлитов.
satelliteKey [String](https://learn.microsoft.com/dotnet/api/system.string)
     Ключ, по которому список карточек-сателлитов содержится в основной карточке. Ключ должен быть уникален для списка 
satelliteCardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор удаляемых карточек-сателлитов.
isNot [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Инвертирует условие поиска удаляемых карточек-сателлитов, т.е. будут удалены все карточки-сателлиты имеющие тип отличный от указанного.
##  __См. также
#### Ссылки
[CardSatelliteHelper -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteHelper.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
