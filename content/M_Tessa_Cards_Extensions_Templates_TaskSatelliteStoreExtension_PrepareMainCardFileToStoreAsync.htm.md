# TaskSatelliteStoreExtension.PrepareMainCardFileToStoreAsync - метод
Выполняет подготовку для заданного файла, сохраняемого с карточкой-сателлитом,
но для которого известно, что он является файлом основной карточки. Например,
устанавливается категория файла в основной карточке.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract ValueTask PrepareMainCardFileToStoreAsync(
    	ICardStoreExtensionContext context,
    	Card satellite,
    	CardFile file
    )
VB __Копировать
     Protected MustOverride Function PrepareMainCardFileToStoreAsync ( 
    	context As ICardStoreExtensionContext,
    	satellite As Card,
    	file As CardFile
    ) As ValueTask
C++ __Копировать
     protected:
    virtual ValueTask PrepareMainCardFileToStoreAsync(
    	ICardStoreExtensionContext^ context, 
    	Card^ satellite, 
    	CardFile^ file
    ) abstract
F# __Копировать
     abstract PrepareMainCardFileToStoreAsync : 
            context : ICardStoreExtensionContext * 
            satellite : Card * 
            file : CardFile -> ValueTask 
#### Параметры
context
[ICardStoreExtensionContext](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm)
    Контекст расширения по сохранению карточки-сателлита.
satellite [Card](T_Tessa_Cards_Card.htm)
    Сохраняемая карточка-сателлит.
file [CardFile](T_Tessa_Cards_CardFile.htm)
    Сохраняемый файл, для которого необходимо вернуть признак принадлежности.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)
##  __См. также
#### Ссылки
[TaskSatelliteStoreExtension -
](T_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
