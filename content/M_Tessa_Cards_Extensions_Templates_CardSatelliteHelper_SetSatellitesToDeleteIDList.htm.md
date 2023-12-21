# CardSatelliteHelper.SetSatellitesToDeleteIDList - метод
Устанавливает список идентификаторов для сателлитов, которые должны быть
удалены из указанного в satelliteKey списка сателлитов.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetSatellitesToDeleteIDList(
    	CardStoreRequest storeRequest,
    	IList satellitesToDeleteID,
    	string satelliteKey
    )
VB __Копировать
     Public Shared Sub SetSatellitesToDeleteIDList ( 
    	storeRequest As CardStoreRequest,
    	satellitesToDeleteID As IList,
    	satelliteKey As String
    )
C++ __Копировать
     public:
    static void SetSatellitesToDeleteIDList(
    	CardStoreRequest^ storeRequest, 
    	IList^ satellitesToDeleteID, 
    	String^ satelliteKey
    )
F# __Копировать
     static member SetSatellitesToDeleteIDList : 
            storeRequest : CardStoreRequest * 
            satellitesToDeleteID : IList * 
            satelliteKey : string -> unit 
#### Параметры
storeRequest [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
    Список содержится в CardStoreRequest.Info.
satellitesToDeleteID
[IList](https://learn.microsoft.com/dotnet/api/system.collections.ilist)
    Cписок идентификаторов
satelliteKey [String](https://learn.microsoft.com/dotnet/api/system.string)
    Ключ со списком карточек-сателлитов, к которому относится список удаляемых сателлитов.
##  __См. также
#### Ссылки
[CardSatelliteHelper -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteHelper.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
