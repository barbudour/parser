# ICardStoreCachingStrategy.AddRowRemover - метод
Добавляет в кэш объект, выполняющий удаление строк из заданной коллекционной
или древовидной секции. Если к кэшу в момент добавления осуществляется
параллельный доступ, то фактическое добавление не гарантируется.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     void AddRowRemover(
    	Guid sectionID,
    	CardSectionRowRemover rowRemover
    )
VB __Копировать
     Sub AddRowRemover ( 
    	sectionID As Guid,
    	rowRemover As CardSectionRowRemover
    )
C++ __Копировать
     void AddRowRemover(
    	Guid sectionID, 
    	CardSectionRowRemover^ rowRemover
    )
F# __Копировать
     abstract AddRowRemover : 
            sectionID : Guid * 
            rowRemover : CardSectionRowRemover -> unit 
#### Параметры
sectionID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор коллекционной или древовидной секции, из которой требуется удалять строки.
rowRemover
[CardSectionRowRemover](T_Tessa_Cards_ComponentModel_CardSectionRowRemover.htm)
    Объект, выполняющий удаление строк из заданной коллекционной или древовидной секции.
##  __См. также
#### Ссылки
[ICardStoreCachingStrategy -
](T_Tessa_Cards_ComponentModel_ICardStoreCachingStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
