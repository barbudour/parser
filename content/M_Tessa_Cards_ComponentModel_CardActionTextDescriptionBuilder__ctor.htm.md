# CardActionTextDescriptionBuilder - конструктор
Создаёт экземпляр класса с указанием метаинформации по типам карточек.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardActionTextDescriptionBuilder(
    	ICardMetadata cardMetadata,
    	ISession session,
    	ICardFileSourceSettings fileSourceSettings
    )
VB __Копировать
     Public Sub New ( 
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	fileSourceSettings As ICardFileSourceSettings
    )
C++ __Копировать
     public:
    CardActionTextDescriptionBuilder(
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	ICardFileSourceSettings^ fileSourceSettings
    )
F# __Копировать
     new : 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            fileSourceSettings : ICardFileSourceSettings -> CardActionTextDescriptionBuilder
#### Параметры
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия пользователя, для которого выводятся текстовые описания.
fileSourceSettings
[ICardFileSourceSettings](T_Tessa_Cards_ICardFileSourceSettings.htm)
    Настройки по местоположениям файлов.
##  __См. также
#### Ссылки
[CardActionTextDescriptionBuilder -
](T_Tessa_Cards_ComponentModel_CardActionTextDescriptionBuilder.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
