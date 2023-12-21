# CardTypeMetadataExtension.GetCardTypesOnServerAsync - метод
Возвращает список всех типов карточек, доступных на сервере в настоящий
момент. При вызове на сервере получает информацию из контекста context, а при
вызове на клиенте - из серверной метаинформации
[ClientCardMetadata](P_Tessa_Cards_Extensions_CardTypeMetadataExtension_ClientCardMetadata.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected ValueTask<CardTypeCollection> GetCardTypesOnServerAsync(
    	ICardMetadataExtensionContext context
    )
VB __Копировать
     Protected Function GetCardTypesOnServerAsync ( 
    	context As ICardMetadataExtensionContext
    ) As ValueTask(Of CardTypeCollection)
C++ __Копировать
     protected:
    ValueTask<CardTypeCollection^> GetCardTypesOnServerAsync(
    	ICardMetadataExtensionContext^ context
    )
F# __Копировать
     member GetCardTypesOnServerAsync : 
            context : ICardMetadataExtensionContext -> ValueTask<CardTypeCollection> 
#### Параметры
context
[ICardMetadataExtensionContext](T_Tessa_Cards_Extensions_ICardMetadataExtensionContext.htm)
    Контекст расширения на метаинформацию.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[CardTypeCollection](T_Tessa_Cards_CardTypeCollection.htm)>  
Список всех типов карточек, доступных на сервере в настоящий момент.
##  __См. также
#### Ссылки
[CardTypeMetadataExtension -
](T_Tessa_Cards_Extensions_CardTypeMetadataExtension.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
