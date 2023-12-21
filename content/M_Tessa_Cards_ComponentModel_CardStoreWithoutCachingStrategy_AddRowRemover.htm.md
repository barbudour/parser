# CardStoreWithoutCachingStrategy.AddRowRemover - метод
Добавляет в кэш объект, выполняющий удаление строк из заданной коллекционной
или древовидной секции. Если к кэшу в момент добавления осуществляется
параллельный доступ, то фактическое добавление не гарантируется.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void AddRowRemover(
    	Guid sectionID,
    	CardSectionRowRemover rowRemover
    )
VB __Копировать
     Public Sub AddRowRemover ( 
    	sectionID As Guid,
    	rowRemover As CardSectionRowRemover
    )
C++ __Копировать
     public:
    virtual void AddRowRemover(
    	Guid sectionID, 
    	CardSectionRowRemover^ rowRemover
    ) sealed
F# __Копировать
     abstract AddRowRemover : 
            sectionID : Guid * 
            rowRemover : CardSectionRowRemover -> unit 
    override AddRowRemover : 
            sectionID : Guid * 
            rowRemover : CardSectionRowRemover -> unit 
#### Параметры
sectionID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор коллекционной или древовидной секции, из которой требуется удалять строки.
rowRemover
[CardSectionRowRemover](T_Tessa_Cards_ComponentModel_CardSectionRowRemover.htm)
    Объект, выполняющий удаление строк из заданной коллекционной или древовидной секции.
#### Реализации
[ICardStoreCachingStrategy.AddRowRemover(Guid,
CardSectionRowRemover)](M_Tessa_Cards_ComponentModel_ICardStoreCachingStrategy_AddRowRemover.htm)  
##  __См. также
#### Ссылки
[CardStoreWithoutCachingStrategy -
](T_Tessa_Cards_ComponentModel_CardStoreWithoutCachingStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
