# CardLoader - конструктор
Создаёт экземпляр класса с указанием информации по загружаемым секциям
карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardLoader(
    	CardLoaderSectionInfo[] sectionsInfo,
    	CardSection[] virtualSections
    )
VB __Копировать
     Public Sub New ( 
    	sectionsInfo As CardLoaderSectionInfo(),
    	virtualSections As CardSection()
    )
C++ __Копировать
     public:
    CardLoader(
    	array<CardLoaderSectionInfo^>^ sectionsInfo, 
    	array<CardSection^>^ virtualSections
    )
F# __Копировать
     new : 
            sectionsInfo : CardLoaderSectionInfo[] * 
            virtualSections : CardSection[] -> CardLoader
#### Параметры
sectionsInfo
[CardLoaderSectionInfo](T_Tessa_Cards_ComponentModel_CardLoaderSectionInfo.htm)[]
    Информация по загружаемым секциям карточки.
virtualSections [CardSection](T_Tessa_Cards_CardSection.htm)[]
    Виртуальные секции карточки.
##  __См. также
#### Ссылки
[CardLoader - ](T_Tessa_Cards_ComponentModel_CardLoader.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
