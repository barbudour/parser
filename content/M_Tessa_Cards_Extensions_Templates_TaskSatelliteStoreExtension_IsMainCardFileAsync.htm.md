# TaskSatelliteStoreExtension.IsMainCardFileAsync - метод
Возвращает признак того, что заданный файл, сохраняемый с карточкой-
сателлитом, на самом деле относится к основной карточке.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract ValueTask<bool> IsMainCardFileAsync(
    	ICardStoreExtensionContext context,
    	Card satellite,
    	CardFile file
    )
VB __Копировать
     Protected MustOverride Function IsMainCardFileAsync ( 
    	context As ICardStoreExtensionContext,
    	satellite As Card,
    	file As CardFile
    ) As ValueTask(Of Boolean)
C++ __Копировать
     protected:
    virtual ValueTask<bool> IsMainCardFileAsync(
    	ICardStoreExtensionContext^ context, 
    	Card^ satellite, 
    	CardFile^ file
    ) abstract
F# __Копировать
     abstract IsMainCardFileAsync : 
            context : ICardStoreExtensionContext * 
            satellite : Card * 
            file : CardFile -> ValueTask<bool> 
#### Параметры
context
[ICardStoreExtensionContext](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm)
    Контекст расширения по сохранению карточки-сателлита.
satellite [Card](T_Tessa_Cards_Card.htm)
    Сохраняемая карточка-сателлит.
file [CardFile](T_Tessa_Cards_CardFile.htm)
    Сохраняемый файл, для которого необходимо вернуть признак принадлежности.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если заданный файл, сохраняемый с карточкой-сателлитом, на самом деле
относится к основной карточке; false в противном случае.
## __См. также
#### Ссылки
[TaskSatelliteStoreExtension -
](T_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
