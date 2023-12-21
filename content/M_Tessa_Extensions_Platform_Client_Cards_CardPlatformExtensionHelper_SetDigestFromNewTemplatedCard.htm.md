# CardPlatformExtensionHelper.SetDigestFromNewTemplatedCard - метод
Устанавливает Digest для ещё не сохранённой карточки шаблона, для которой
файлы загружаются через
[ExternalSource](P_Tessa_Cards_CardFile_ExternalSource.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Cards](N_Tessa_Extensions_Platform_Client_Cards.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool SetDigestFromNewTemplatedCard(
    	CardRequestBase request
    )
VB __Копировать
     Public Shared Function SetDigestFromNewTemplatedCard ( 
    	request As CardRequestBase
    ) As Boolean
C++ __Копировать
     public:
    static bool SetDigestFromNewTemplatedCard(
    	CardRequestBase^ request
    )
F# __Копировать
     static member SetDigestFromNewTemplatedCard : 
            request : CardRequestBase -> bool 
#### Параметры
request [CardRequestBase](T_Tessa_Cards_CardRequestBase.htm)
    Запрос к сервису карточек, в котором требуется установить Digest.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если Digest был установлен; false, если карточка не является карточкой
шаблона, которая ещё не была сохранена, поэтому Digest не был установлен.
## __См. также
#### Ссылки
[CardPlatformExtensionHelper -
](T_Tessa_Extensions_Platform_Client_Cards_CardPlatformExtensionHelper.htm)
[Tessa.Extensions.Platform.Client.Cards - пространство
имён](N_Tessa_Extensions_Platform_Client_Cards.htm)
