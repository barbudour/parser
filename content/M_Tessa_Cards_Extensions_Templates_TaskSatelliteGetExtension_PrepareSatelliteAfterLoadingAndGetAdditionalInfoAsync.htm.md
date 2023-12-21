#
TaskSatelliteGetExtension.PrepareSatelliteAfterLoadingAndGetAdditionalInfoAsync
- метод
Выполняет постобработку загруженной карточки-сателлита, а также возвращает
дополнительную информацию, такую как токен прав доступа, которая используется
в других методах этого класса, в т.ч. для загрузки основной карточки. Если
такой информации нет, то возвращает null.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract ValueTask<Object> PrepareSatelliteAfterLoadingAndGetAdditionalInfoAsync(
    	ICardGetExtensionContext context,
    	Card satellite
    )
VB __Копировать
     Protected MustOverride Function PrepareSatelliteAfterLoadingAndGetAdditionalInfoAsync ( 
    	context As ICardGetExtensionContext,
    	satellite As Card
    ) As ValueTask(Of Object)
C++ __Копировать
     protected:
    virtual ValueTask<Object^> PrepareSatelliteAfterLoadingAndGetAdditionalInfoAsync(
    	ICardGetExtensionContext^ context, 
    	Card^ satellite
    ) abstract
F# __Копировать
     abstract PrepareSatelliteAfterLoadingAndGetAdditionalInfoAsync : 
            context : ICardGetExtensionContext * 
            satellite : Card -> ValueTask<Object> 
#### Параметры
context
[ICardGetExtensionContext](T_Tessa_Cards_Extensions_ICardGetExtensionContext.htm)
    Контекст расширения по загрузке карточки-сателлита.
satellite [Card](T_Tessa_Cards_Card.htm)
    Загруженная карточка-сателлит.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Object](https://learn.microsoft.com/dotnet/api/system.object)>  
Дополнительная информация, такая как токен прав доступа, которая используется
в других методах этого класса, или null, если такой информации нет.
## __См. также
#### Ссылки
[TaskSatelliteGetExtension -
](T_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
