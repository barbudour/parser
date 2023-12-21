# CardSatelliteHelper.TryGetSingleSatelliteCardFromList - метод
Возвращает карточку-сателлит, которая была установлена в пакете основной
карточки, или null, если карточка-сателлит указанного типа не была найдена в
списке карточек сателлитов доступном по указанному ключу или список карточек
сателлитов не содержит значений.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Card TryGetSingleSatelliteCardFromList(
    	Card mainCard,
    	string satelliteKey,
    	Guid satelliteCardTypeID
    )
VB __Копировать
     Public Shared Function TryGetSingleSatelliteCardFromList ( 
    	mainCard As Card,
    	satelliteKey As String,
    	satelliteCardTypeID As Guid
    ) As Card
C++ __Копировать
     public:
    static Card^ TryGetSingleSatelliteCardFromList(
    	Card^ mainCard, 
    	String^ satelliteKey, 
    	Guid satelliteCardTypeID
    )
F# __Копировать
     static member TryGetSingleSatelliteCardFromList : 
            mainCard : Card * 
            satelliteKey : string * 
            satelliteCardTypeID : Guid -> Card 
#### Параметры
mainCard [Card](T_Tessa_Cards_Card.htm)
    Пакет основной карточки, в которой может быть установлен список карточек-сателлитов.
satelliteKey [String](https://learn.microsoft.com/dotnet/api/system.string)
    Ключ в [Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm) основной карточки, который содержит хранилище карточек-сателлитов.
satelliteCardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа карточки сателлита, который требуется получить.
#### Возвращаемое значение
[Card](T_Tessa_Cards_Card.htm)  
Карточка-сателлит, которая была установлена в пакете основной карточки, или
значение null, если карточка-сателлит не была установлена или не
соответсвовала указаному типу satelliteCardTypeID.
## __Исключения
[InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception)|
Найдено более одной карточки-сателлита указанного типа.  
---|---  
##  __См. также
#### Ссылки
[CardSatelliteHelper -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteHelper.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
