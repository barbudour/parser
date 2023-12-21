# CardSourceContentStrategy - конструктор
Создаёт экземпляр класса с указанием стратегий, используемых для различных
значений перечисления
[CardFileSourceType](T_Tessa_Cards_CardFileSourceType.htm), заданном в
контексте.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardSourceContentStrategy(
    	ICardFileSourceSettings fileSourceSettings,
    	Func<ICardFileSource, ICardContentStrategy> createDatabaseContentStrategyFunc,
    	Func<ICardFileSource, ICardContentStrategy> createFileSystemContentStrategyFunc
    )
VB __Копировать
     Public Sub New ( 
    	fileSourceSettings As ICardFileSourceSettings,
    	createDatabaseContentStrategyFunc As Func(Of ICardFileSource, ICardContentStrategy),
    	createFileSystemContentStrategyFunc As Func(Of ICardFileSource, ICardContentStrategy)
    )
C++ __Копировать
     public:
    CardSourceContentStrategy(
    	ICardFileSourceSettings^ fileSourceSettings, 
    	Func<ICardFileSource^, ICardContentStrategy^>^ createDatabaseContentStrategyFunc, 
    	Func<ICardFileSource^, ICardContentStrategy^>^ createFileSystemContentStrategyFunc
    )
F# __Копировать
     new : 
            fileSourceSettings : ICardFileSourceSettings * 
            createDatabaseContentStrategyFunc : Func<ICardFileSource, ICardContentStrategy> * 
            createFileSystemContentStrategyFunc : Func<ICardFileSource, ICardContentStrategy> -> CardSourceContentStrategy
#### Параметры
fileSourceSettings
[ICardFileSourceSettings](T_Tessa_Cards_ICardFileSourceSettings.htm)
    Настройки для местоположений файлов.
createDatabaseContentStrategyFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[ICardFileSource](T_Tessa_Cards_ICardFileSource.htm),
[ICardContentStrategy](T_Tessa_Cards_ComponentModel_ICardContentStrategy.htm)>
     Функция, которая для заданных настроек местоположения создаёт стратегию, используемую для взаимодействия с контентом файлов в базе данных. 
createFileSystemContentStrategyFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[ICardFileSource](T_Tessa_Cards_ICardFileSource.htm),
[ICardContentStrategy](T_Tessa_Cards_ComponentModel_ICardContentStrategy.htm)>
     Функция, которая для заданных настроек местоположения создаёт стратегию, используемую для взаимодействия с контентом файлов на файловой системе. 
## __См. также
#### Ссылки
[CardSourceContentStrategy -
](T_Tessa_Cards_ComponentModel_CardSourceContentStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
