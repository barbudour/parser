# MultitypeSatelliteDeleteExtension.GetAdditionalInfoForDeletionAsync - метод
Возвращает дополнительную информацию для использования в запросах на удаление
карточек-сателлитов в методе PrepareSatelliteDeleteRequest. Например, это
токен прав доступа. Метод может вернуть null, если такая информация
отсутствует.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual ValueTask<Object> GetAdditionalInfoForDeletionAsync(
    	ICardDeleteExtensionContext context
    )
VB __Копировать
     Protected Overridable Function GetAdditionalInfoForDeletionAsync ( 
    	context As ICardDeleteExtensionContext
    ) As ValueTask(Of Object)
C++ __Копировать
     protected:
    virtual ValueTask<Object^> GetAdditionalInfoForDeletionAsync(
    	ICardDeleteExtensionContext^ context
    )
F# __Копировать
     abstract GetAdditionalInfoForDeletionAsync : 
            context : ICardDeleteExtensionContext -> ValueTask<Object> 
    override GetAdditionalInfoForDeletionAsync : 
            context : ICardDeleteExtensionContext -> ValueTask<Object> 
#### Параметры
context
[ICardDeleteExtensionContext](T_Tessa_Cards_Extensions_ICardDeleteExtensionContext.htm)
    Контекст расширения по удалению основной карточки.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Object](https://learn.microsoft.com/dotnet/api/system.object)>  
Дополнительная информация для использования в запросах на удаление карточек-
сателлитов или null, если такая информация отсутствует.
## __См. также
#### Ссылки
[MultitypeSatelliteDeleteExtension -
](T_Tessa_Cards_Extensions_Templates_MultitypeSatelliteDeleteExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
