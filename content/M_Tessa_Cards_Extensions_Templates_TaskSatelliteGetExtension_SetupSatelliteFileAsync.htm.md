# TaskSatelliteGetExtension.SetupSatelliteFileAsync - метод
Устанавливает свойства загруженного файла в карточке-сателлите для учёта того,
что файл может принадлежать основной карточке.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract ValueTask SetupSatelliteFileAsync(
    	ICardGetExtensionContext context,
    	CardFile file,
    	bool isMainCard
    )
VB __Копировать
     Protected MustOverride Function SetupSatelliteFileAsync ( 
    	context As ICardGetExtensionContext,
    	file As CardFile,
    	isMainCard As Boolean
    ) As ValueTask
C++ __Копировать
     protected:
    virtual ValueTask SetupSatelliteFileAsync(
    	ICardGetExtensionContext^ context, 
    	CardFile^ file, 
    	bool isMainCard
    ) abstract
F# __Копировать
     abstract SetupSatelliteFileAsync : 
            context : ICardGetExtensionContext * 
            file : CardFile * 
            isMainCard : bool -> ValueTask 
#### Параметры
context
[ICardGetExtensionContext](T_Tessa_Cards_Extensions_ICardGetExtensionContext.htm)
    Контекст расширения по загрузке карточки-сателлита.
file [CardFile](T_Tessa_Cards_CardFile.htm)
    Загруженный файл, свойства которого требуется установить.
isMainCard [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Признак того, что файл принадлежит основной карточке, а не карточке-сателлиту.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
##  __См. также
#### Ссылки
[TaskSatelliteGetExtension -
](T_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
