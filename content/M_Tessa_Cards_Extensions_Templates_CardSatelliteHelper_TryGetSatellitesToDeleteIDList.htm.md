# CardSatelliteHelper.TryGetSatellitesToDeleteIDList - метод
Получает список идентификаторов для сателлитов из CardStoreRequest, которые
должны быть удалены из указанного в satelliteKey списка сателлитов
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IList<Guid> TryGetSatellitesToDeleteIDList(
    	CardStoreRequest storeRequest,
    	string satelliteKey
    )
VB __Копировать
     Public Shared Function TryGetSatellitesToDeleteIDList ( 
    	storeRequest As CardStoreRequest,
    	satelliteKey As String
    ) As IList(Of Guid)
C++ __Копировать
     public:
    static IList<Guid>^ TryGetSatellitesToDeleteIDList(
    	CardStoreRequest^ storeRequest, 
    	String^ satelliteKey
    )
F# __Копировать
     static member TryGetSatellitesToDeleteIDList : 
            storeRequest : CardStoreRequest * 
            satelliteKey : string -> IList<Guid> 
#### Параметры
storeRequest [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
    Список содержится в CardStoreRequest.Info.
satelliteKey [String](https://learn.microsoft.com/dotnet/api/system.string)
    Ключ со списком карточек-сателлитов, к которому относится список удаляемых сателлитов.
#### Возвращаемое значение
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>  
Список идентификаторов.
##  __См. также
#### Ссылки
[CardSatelliteHelper -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteHelper.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
