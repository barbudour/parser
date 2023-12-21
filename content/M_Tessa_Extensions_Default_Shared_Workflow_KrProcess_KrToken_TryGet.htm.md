# KrToken.TryGet(IDictionary<String, Object>) - метод
Возвращает информацию по токену безопасности
[KrToken](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrToken.htm)
или null, если такая информация не была установлена.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static KrToken TryGet(
    	IDictionary<string, Object> cardInfo
    )
VB __Копировать
     Public Shared Function TryGet ( 
    	cardInfo As IDictionary(Of String, Object)
    ) As KrToken
C++ __Копировать
     public:
    static KrToken^ TryGet(
    	IDictionary<String^, Object^>^ cardInfo
    )
F# __Копировать
     static member TryGet : 
            cardInfo : IDictionary<string, Object> -> KrToken 
#### Параметры
cardInfo
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
     Дополнительная информация для карточки. Это либо card.Info для загруженной карточки (например, в [CardGetResponse](T_Tessa_Cards_CardGetResponse.htm)) или карточки, отправляемой на сохранение в [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm). Либо request.Info для всех других запросов к [ICardRepository](T_Tessa_Cards_ICardRepository.htm), в которых нет карточки. 
#### Возвращаемое значение
[KrToken](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrToken.htm)  
Запрошенная информация или null, если требуемая информация ещё не была
установлена.
##  __См. также
#### Ссылки
[KrToken - ](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrToken.htm)
[TryGet -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrToken_TryGet.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
