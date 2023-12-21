# PlatformCardExtensionHelper - класс
Вспомогательные средства, связанные с карточками шаблонов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Cards](N_Tessa_Extensions_Platform_Client_Cards.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static class PlatformCardExtensionHelper
VB __Копировать
     Public NotInheritable Class PlatformCardExtensionHelper
C++ __Копировать
     public ref class PlatformCardExtensionHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type PlatformCardExtensionHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PlatformCardExtensionHelper
##  __Методы
[CreateFromTemplateAsync](M_Tessa_Extensions_Platform_Client_Cards_PlatformCardExtensionHelper_CreateFromTemplateAsync.htm)|
Создаёт карточку по шаблону на основании шаблона карточки и открывает её в
отдельной вкладке.  
---|---  
[DeleteDeletedCardAsync](M_Tessa_Extensions_Platform_Client_Cards_PlatformCardExtensionHelper_DeleteDeletedCardAsync.htm)|
Выполняет удаление удалённой карточки из корзины.  
[EditCardInTemplateAsync](M_Tessa_Extensions_Platform_Client_Cards_PlatformCardExtensionHelper_EditCardInTemplateAsync.htm)|
Запускает редактирование карточки в шаблоне для текущего объекта редактора
editor, в котором должен быть открыт шаблон карточки.  
[GetToolbarItemsForEditorInTemplate](M_Tessa_Extensions_Platform_Client_Cards_PlatformCardExtensionHelper_GetToolbarItemsForEditorInTemplate.htm)|
Создаёт список действий на верхней панели тулбара для карточки, редактируемой
в шаблоне.  
[OpenDeletedCardAsync](M_Tessa_Extensions_Platform_Client_Cards_PlatformCardExtensionHelper_OpenDeletedCardAsync.htm)|
Выполняет просмотр удалённой карточки.  
[RepairDeletedCardAsync](M_Tessa_Extensions_Platform_Client_Cards_PlatformCardExtensionHelper_RepairDeletedCardAsync.htm)|
Исправляет структуру удалённой карточки.  
[RepairTemplateAsync](M_Tessa_Extensions_Platform_Client_Cards_PlatformCardExtensionHelper_RepairTemplateAsync.htm)|
Исправляет структуру карточки в шаблоне.  
[RestoreDeletedCardAsync](M_Tessa_Extensions_Platform_Client_Cards_PlatformCardExtensionHelper_RestoreDeletedCardAsync.htm)|
Восстанавливает удалённую карточку из корзины.  
[ReturnToDeletedCardAsync](M_Tessa_Extensions_Platform_Client_Cards_PlatformCardExtensionHelper_ReturnToDeletedCardAsync.htm)|
Переходит из просмотра удалённой карточки в собственно удалённую карточку.  
[ReturnToTemplateAsync](M_Tessa_Extensions_Platform_Client_Cards_PlatformCardExtensionHelper_ReturnToTemplateAsync.htm)|
Возвращается из карточки, редактируемой в шаблоне, к шаблону карточки для
текущего объекта редактора editor, в котором должна редактироваться карточка в
шаблоне, открытая посредством [EditCardInTemplateAsync(ICardEditorModel,
ICardUIManager, IUIHost,
CancellationToken)](M_Tessa_Extensions_Platform_Client_Cards_PlatformCardExtensionHelper_EditCardInTemplateAsync.htm).  
## __Поля
[CardInTemplateKey](F_Tessa_Extensions_Platform_Client_Cards_PlatformCardExtensionHelper_CardInTemplateKey.htm)|
Ключ, по которому располагается карточка в шаблоне при сохранении в свойстве
[Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm), если сохранение
выполняется из этой карточки, а не из карточки шаблона. Расширение
[CardTemplateStoreExtension](T_Tessa_Extensions_Platform_Client_Cards_CardTemplateStoreExtension.htm)
после работы удаляет эту карточку.  
---|---  
[DeletedIDKey](F_Tessa_Extensions_Platform_Client_Cards_PlatformCardExtensionHelper_DeletedIDKey.htm)|
Идентификатор удалённой карточки
[Guid](https://learn.microsoft.com/dotnet/api/system.guid) в модели
CardModel.Info для вкладки с просмотром удалённой карточки.  
[OpeningCardFromTemplateKey](F_Tessa_Extensions_Platform_Client_Cards_PlatformCardExtensionHelper_OpeningCardFromTemplateKey.htm)|
Признак того, что открывается карточка, редактируемая в шаблоне.
Устанавливается в запросе на открытие
[Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm).  
[OriginalCardOpenedName](F_Tessa_Extensions_Platform_Client_Cards_PlatformCardExtensionHelper_OriginalCardOpenedName.htm)|
Описание вкладки, в которой открыт просмотр удалённой карточки.  
[OriginalCardOpenedStatus](F_Tessa_Extensions_Platform_Client_Cards_PlatformCardExtensionHelper_OriginalCardOpenedStatus.htm)|
Текст в статусной строки для вкладки, в которой открыт просмотр удалённой
карточки.  
[TemplateCardKey](F_Tessa_Extensions_Platform_Client_Cards_PlatformCardExtensionHelper_TemplateCardKey.htm)|
Ключ, по которому располагается загруженная карточка шаблона в свойстве
[Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm).  
[TemplateOriginalCardIDKey](F_Tessa_Extensions_Platform_Client_Cards_PlatformCardExtensionHelper_TemplateOriginalCardIDKey.htm)|
Изначальный идентификатор карточки в шаблоне в свойстве
[Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm) при загрузке карточки
шаблона. Этот идентификатор будет восстановлен при сохранении карточки.  
[TemplateOriginalPermissions](F_Tessa_Extensions_Platform_Client_Cards_PlatformCardExtensionHelper_TemplateOriginalPermissions.htm)|
Изначальные разрешения для карточки в шаблоне в свойстве
[Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm) при загрузке карточки
шаблона. Эти разрешения будут восстановлены при сохранении карточки.  
[TemplateSectionRowsKey](F_Tessa_Extensions_Platform_Client_Cards_PlatformCardExtensionHelper_TemplateSectionRowsKey.htm)|
Ключ, по которому располагаются секции коллекционных и древовидных секций для
загруженной карточки шаблона в свойстве
[Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm).  
## __См. также
#### Ссылки
[Tessa.Extensions.Platform.Client.Cards - пространство
имён](N_Tessa_Extensions_Platform_Client_Cards.htm)
