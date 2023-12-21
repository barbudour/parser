# TileNames - класс
Имена стандартных плиток, которые создаются платформенными расширениями или
расширениями типового решения.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class TileNames
VB __Копировать
     Public NotInheritable Class TileNames
C++ __Копировать
     public ref class TileNames abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type TileNames = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TileNames
##  __Поля
[About](F_Tessa_Platform_TileNames_About.htm)|  Плитка верхнего уровня "О
программе" на правой боковой панели.  
---|---  
[Acquaintance](F_Tessa_Platform_TileNames_Acquaintance.htm)|  Плитка
"Отправить" для массового ознакомления, вложенная в группу
[AcquaintanceGroup](F_Tessa_Platform_TileNames_AcquaintanceGroup.htm).  
[AcquaintanceGroup](F_Tessa_Platform_TileNames_AcquaintanceGroup.htm)|  Плитка
верхнего уровня на левой боковой панели, группирующая плитки для массового
ознакомления.  
[AcquaintanceHistory](F_Tessa_Platform_TileNames_AcquaintanceHistory.htm)|
Плитка "История" для массового ознакомления, вложенная в группу
[AcquaintanceGroup](F_Tessa_Platform_TileNames_AcquaintanceGroup.htm).  
[ActionsGrouping](F_Tessa_Platform_TileNames_ActionsGrouping.htm)|  Плитка
верхнего уровня для дополнительных действий с карточкой, которые автоматически
группируются.  
[AddSearchQuery](F_Tessa_Platform_TileNames_AddSearchQuery.htm)|  Дочерняя
плитка для [TreeSettings](F_Tessa_Platform_TileNames_TreeSettings.htm)
Добавить поисковый запрос  
[BackToTemplate](F_Tessa_Platform_TileNames_BackToTemplate.htm)|  Плитка
верхнего уровня для возврата к карточке шаблона из карточки, редактируемой
внутри шаблона.  
[Cancel](F_Tessa_Platform_TileNames_Cancel.htm)|  Кнопка тулбара для закрытия
диалога без сохранения изменений  
[CardActionHistory](F_Tessa_Platform_TileNames_CardActionHistory.htm)|  Плитка
на уровне [CardTools](F_Tessa_Platform_TileNames_CardTools.htm) для
отображения истории действий по карточке.  
[CardOthers](F_Tessa_Platform_TileNames_CardOthers.htm)|  Плитка верхнего
уровня для прочих действий с карточкой.  
[CardTools](F_Tessa_Platform_TileNames_CardTools.htm)|  Плитка верхнего уровня
для административных инструментов.  
[ChangeParticipants](F_Tessa_Platform_TileNames_ChangeParticipants.htm)|
Плитка изменить участника форума  
[CheckTasks](F_Tessa_Platform_TileNames_CheckTasks.htm)|  Плитка верхнего
уровня на правой боковой панели для проверки наличия новых заданий вручную.  
[ChooseWallpaper](F_Tessa_Platform_TileNames_ChooseWallpaper.htm)|  Плитка для
выбора файла с фоном приложения, доступная в группе
[SelectWallpaper](F_Tessa_Platform_TileNames_SelectWallpaper.htm).  
[CloseSession](F_Tessa_Platform_TileNames_CloseSession.htm)|  Плитка верхнего
уровня для закрытия сессий из представления "Сессии".  
[CopyCardLink](F_Tessa_Platform_TileNames_CopyCardLink.htm)|  Плитка на уровне
[CardOthers](F_Tessa_Platform_TileNames_CardOthers.htm) для копирования ссылки
на карточку.  
[CreateCard](F_Tessa_Platform_TileNames_CreateCard.htm)|  Плитка верхнего
уровня, выводящая сгруппированный список плиток для создания карточек
различных типов.  
[CreateCardBasedOn](F_Tessa_Platform_TileNames_CreateCardBasedOn.htm)|  Плитка
"Создать на основании", вложенная в
[CardOthers](F_Tessa_Platform_TileNames_CardOthers.htm).  
[CreateCardCopy](F_Tessa_Platform_TileNames_CreateCardCopy.htm)|  Плитка на
уровне [CardOthers](F_Tessa_Platform_TileNames_CardOthers.htm) для создания
копии редактируемой карточки.  
[CreateCardFromTemplate](F_Tessa_Platform_TileNames_CreateCardFromTemplate.htm)|
Плитка верхнего уровня для создания карточки из шаблона.  
[CreateCardMore](F_Tessa_Platform_TileNames_CreateCardMore.htm)|  Плитка
внутри [CreateCard](F_Tessa_Platform_TileNames_CreateCard.htm), которая
отображается, если в группе типов карточек количество плиток больше
допустимого.  
[CreateCardTemplate](F_Tessa_Platform_TileNames_CreateCardTemplate.htm)|
Плитка на уровне [CardOthers](F_Tessa_Platform_TileNames_CardOthers.htm) для
создания шаблона редактируемой карточки.  
[CreateFileFromTemplate](F_Tessa_Platform_TileNames_CreateFileFromTemplate.htm)|
Плитка верхнего уровня на левой панели для создания файлов по шаблону  
[CreateFolder](F_Tessa_Platform_TileNames_CreateFolder.htm)|  Дочерняя плитка
для [TreeSettings](F_Tessa_Platform_TileNames_TreeSettings.htm) Создание папки  
[CreateMultipleCards](F_Tessa_Platform_TileNames_CreateMultipleCards.htm)|
Плитка верхнего уровня на левой панели для создания сразу нескольких карточек
по шаблону. Такая группа может переместиться в плитку действий
[ActionsGrouping](F_Tessa_Platform_TileNames_ActionsGrouping.htm), но
обращаться к ней нужно именно на верхнем уровне.  
[DeleteCard](F_Tessa_Platform_TileNames_DeleteCard.htm)|  Плитка на уровне
[CardOthers](F_Tessa_Platform_TileNames_CardOthers.htm) для удаления карточки.  
[DeleteCardFromView](F_Tessa_Platform_TileNames_DeleteCardFromView.htm)|
Плитка на уровне [ViewsOther](F_Tessa_Platform_TileNames_ViewsOther.htm) для
удаления карточек из представления.  
[DeleteNotificationSubscription](F_Tessa_Platform_TileNames_DeleteNotificationSubscription.htm)|
Плитка верхнего уровня для удаление подписок на уведомления из представления
"Подписки на уведомления".  
[DeleteTreeItem](F_Tessa_Platform_TileNames_DeleteTreeItem.htm)|  Дочерняя
плитка для [TreeSettings](F_Tessa_Platform_TileNames_TreeSettings.htm) Удалить
текущий узел  
[Dialogues](F_Tessa_Platform_TileNames_Dialogues.htm)|  Плитка верхнего
уровня, группирующая диалоговые окна.  
[DictionaryTypes](F_Tessa_Platform_TileNames_DictionaryTypes.htm)|  Плитка,
вложенная в [CreateCard](F_Tessa_Platform_TileNames_CreateCard.htm) и
группирующая все типы карточек, относящиеся к справочникам.  
[DocumentTypes](F_Tessa_Platform_TileNames_DocumentTypes.htm)|  Плитка,
вложенная в [CreateCard](F_Tessa_Platform_TileNames_CreateCard.htm) и
группирующая все типы карточек, относящиеся к документам.  
[EditCardInTemplate](F_Tessa_Platform_TileNames_EditCardInTemplate.htm)|
Плитка верхнего уровня для редактирования карточки в шаблоне.  
[ExpandChart](F_Tessa_Platform_TileNames_ExpandChart.htm)|  Плитка экспорта
диаграмм на левой боковой панели.  
[ExportAllCardsFromView](F_Tessa_Platform_TileNames_ExportAllCardsFromView.htm)|
Плитка, вложенная в [ViewsOther](F_Tessa_Platform_TileNames_ViewsOther.htm),
для экспорта всех карточек из представления.  
[ExportAllCharts](F_Tessa_Platform_TileNames_ExportAllCharts.htm)|  Плитка
экспорта диаграмм на левой боковой панели.  
[ExportAllChartsCopyToClipboard](F_Tessa_Platform_TileNames_ExportAllChartsCopyToClipboard.htm)|
Плитка экспорта диаграмм на левой боковой панели.  
[ExportAllChartsSelectFile](F_Tessa_Platform_TileNames_ExportAllChartsSelectFile.htm)|
Плитка экспорта диаграмм на левой боковой панели.  
[ExportCard](F_Tessa_Platform_TileNames_ExportCard.htm)|  Плитка на уровне
[CardTools](F_Tessa_Platform_TileNames_CardTools.htm) для административного
экспорта карточки.  
[ExportCardFromView](F_Tessa_Platform_TileNames_ExportCardFromView.htm)|
Плитка, вложенная в [ViewsOther](F_Tessa_Platform_TileNames_ViewsOther.htm),
для экспорта выбранных карточек из представления.  
[ExportChart](F_Tessa_Platform_TileNames_ExportChart.htm)|  Плитка экспорта
диаграмм на левой боковой панели.  
[ExportChartCopyToClipboard](F_Tessa_Platform_TileNames_ExportChartCopyToClipboard.htm)|
Плитка экспорта диаграмм на левой боковой панели.  
[ExportChartSelectFile](F_Tessa_Platform_TileNames_ExportChartSelectFile.htm)|
Плитка экспорта диаграмм на левой боковой панели.  
[FilterView](F_Tessa_Platform_TileNames_FilterView.htm)|  Плитка вложенная в
[ViewsOther](F_Tessa_Platform_TileNames_ViewsOther.htm) для фильтрации
представления.  
[GenerateTestCards](F_Tessa_Platform_TileNames_GenerateTestCards.htm)|  Плитка
верхнего уровня "Создание карточек для тестирования" на левой боковой панели
для карточки "Типовое решение".  
[Help](F_Tessa_Platform_TileNames_Help.htm)|  Плитка верхнего уровня "Справка"
на правой боковой панели.  
[HideEmptyFolders](F_Tessa_Platform_TileNames_HideEmptyFolders.htm)|  Плитка
вложенная в [ViewsOther](F_Tessa_Platform_TileNames_ViewsOther.htm) скрыть
пустые папки  
[HideInaccessibleItems](F_Tessa_Platform_TileNames_HideInaccessibleItems.htm)|
Дочерняя плитка для
[TreeSettings](F_Tessa_Platform_TileNames_TreeSettings.htm) Cкрыть недоступные
элементы  
[HideTree](F_Tessa_Platform_TileNames_HideTree.htm)|  Плитка вложенная в
[ViewsOther](F_Tessa_Platform_TileNames_ViewsOther.htm) скрыть дерево
представлений  
[ImportCardDialog](F_Tessa_Platform_TileNames_ImportCardDialog.htm)|  Плитка,
вложенная в [Dialogues](F_Tessa_Platform_TileNames_Dialogues.htm) и
отображающая диалог административного импорта карточек.  
[MySettings](F_Tessa_Platform_TileNames_MySettings.htm)|  Плитка верхнего
уровня на правой панели для открытия диалога "Мои настройки".  
[NewUsersSettings](F_Tessa_Platform_TileNames_NewUsersSettings.htm)|  Плитка,
вложенная в [MySettings](F_Tessa_Platform_TileNames_MySettings.htm), для
открытия диалога "Мои настройки" с редактированием настроек для новых
сотрудников.  
[NotificationSubscriptions](F_Tessa_Platform_TileNames_NotificationSubscriptions.htm)|
Плитка верхнего уровня, при нажатии на которую открываются настройки
подписок/отписок для карточки.  
[OpenCardFromActionHistory](F_Tessa_Platform_TileNames_OpenCardFromActionHistory.htm)|
Плитка верхнего уровня на левой панели для открытия карточки из представления
с историей действий.  
[OpenTemplateFromView](F_Tessa_Platform_TileNames_OpenTemplateFromView.htm)|
Плитка верхнего уровня для открытия карточки шаблона из представления.  
[OtherTypes](F_Tessa_Platform_TileNames_OtherTypes.htm)|  Плитка, вложенная в
[CreateCard](F_Tessa_Platform_TileNames_CreateCard.htm) и группирующая все
типы карточек, у которых не была указана группа.  
[PrintAllCharts](F_Tessa_Platform_TileNames_PrintAllCharts.htm)|  Плитка
верхнего уровня "Печать диаграмм" на левой боковой панели.  
[PrintBarcode](F_Tessa_Platform_TileNames_PrintBarcode.htm)|  Плитка верхнего
уровня "Печать штрих-кода" на левой боковой панели.  
[PrintBarcodeSelectPrinter](F_Tessa_Platform_TileNames_PrintBarcodeSelectPrinter.htm)|
Плитка, вложенная в
[PrintBarcode](F_Tessa_Platform_TileNames_PrintBarcode.htm), для выбора
принтера.  
[PrintChart](F_Tessa_Platform_TileNames_PrintChart.htm)|  Плитка верхнего
уровня "Печать диаграммы" на левой боковой панели.  
[RefreshAll](F_Tessa_Platform_TileNames_RefreshAll.htm)|  Плитка верхнего
уровня обновить представление и узел  
[RefreshCard](F_Tessa_Platform_TileNames_RefreshCard.htm)|  Плитка верхнего
уровня и кнопка тулбара для обновления карточки.  
[RefreshNode](F_Tessa_Platform_TileNames_RefreshNode.htm)|  Плитка вложенная в
[ViewsOther](F_Tessa_Platform_TileNames_ViewsOther.htm) для обновления
текущего узла дерева  
[RefreshView](F_Tessa_Platform_TileNames_RefreshView.htm)|  Плитка вложенная в
[ViewsOther](F_Tessa_Platform_TileNames_ViewsOther.htm) для обновления
представления.  
[RemoveOperation](F_Tessa_Platform_TileNames_RemoveOperation.htm)|  Плитка
верхнего уровня для удаления операции из представления "Активные операции".  
[RemoveParticipants](F_Tessa_Platform_TileNames_RemoveParticipants.htm)|
Плитка удалить участника форума  
[RepairDeleted](F_Tessa_Platform_TileNames_RepairDeleted.htm)|  Плитка
верхнего уровня для исправления удалённой карточки.  
[RepairDeletedFromView](F_Tessa_Platform_TileNames_RepairDeletedFromView.htm)|
Плитка верхнего уровня для исправления удалённой карточки из представления.  
[RepairTemplate](F_Tessa_Platform_TileNames_RepairTemplate.htm)|  Плитка
верхнего уровня для исправления карточки шаблона.  
[RepairTemplateFromView](F_Tessa_Platform_TileNames_RepairTemplateFromView.htm)|
Плитка верхнего уровня для исправления карточки шаблона из представления.  
[ResetLayoutSettings](F_Tessa_Platform_TileNames_ResetLayoutSettings.htm)|
Плитка, вложенная в [ViewsOther](F_Tessa_Platform_TileNames_ViewsOther.htm),
для сброса настроек макета  
[RestoreCardFromDeleted](F_Tessa_Platform_TileNames_RestoreCardFromDeleted.htm)|
Плитка верхнего уровня для восстановления удалённой карточки.  
[RestoreCardFromView](F_Tessa_Platform_TileNames_RestoreCardFromView.htm)|
Плитка верхнего уровня для восстановления карточек из представления "Удалённые
карточки".  
[ReturnToDeleted](F_Tessa_Platform_TileNames_ReturnToDeleted.htm)|  Плитка
верхнего уровня на левой панели для возврата из режима просмотра удалённой
карточки в собственно удалённую карточку.  
[RoleDeputiesManagement](F_Tessa_Platform_TileNames_RoleDeputiesManagement.htm)|
Плитка, вложенная в [Dialogues](F_Tessa_Platform_TileNames_Dialogues.htm) и
отображающая карточку "Мои замещения".  
[RoleTypes](F_Tessa_Platform_TileNames_RoleTypes.htm)|  Плитка, вложенная в
[CreateCard](F_Tessa_Platform_TileNames_CreateCard.htm) и группирующая все
типы карточек, относящиеся к ролям.  
[SaveAndCloseCard](F_Tessa_Platform_TileNames_SaveAndCloseCard.htm)|  Плитка
верхнего уровня и кнопка тулбар адля сохранения карточки и закрытия рабочей
области.  
[SaveCard](F_Tessa_Platform_TileNames_SaveCard.htm)|  Плитка верхнего уровня и
кнопка тулбара для сохранения карточки.  
[SaveCloseAndCreateCard](F_Tessa_Platform_TileNames_SaveCloseAndCreateCard.htm)|
Плитка верхнего уровня для сохранения карточки с дальнейшим закрытием и
созданием такой же карточки.  
[SaveLayoutSettings](F_Tessa_Platform_TileNames_SaveLayoutSettings.htm)|
Плитка, вложенная в [ViewsOther](F_Tessa_Platform_TileNames_ViewsOther.htm),
для сохранения настроек макета  
[SaveWorkplaceSettings](F_Tessa_Platform_TileNames_SaveWorkplaceSettings.htm)|
Плитка вложенная в [ViewsOther](F_Tessa_Platform_TileNames_ViewsOther.htm)
Сохранить настройки рабочего места  
[SearchQueries](F_Tessa_Platform_TileNames_SearchQueries.htm)|  Плитка,
вложенная в [Dialogues](F_Tessa_Platform_TileNames_Dialogues.htm) и
предназначенная для управления поисковыми запросами  
[SelectTheme](F_Tessa_Platform_TileNames_SelectTheme.htm)|  Плитка,
группирующая выбор темы приложения, доступная в группе
[SelectWallpaper](F_Tessa_Platform_TileNames_SelectWallpaper.htm).  
[SelectWallpaper](F_Tessa_Platform_TileNames_SelectWallpaper.htm)|  Плитка
верхнего уровня на правой боковой панели, группирующая выбор фона приложения.  
[SendProtocolTasks](F_Tessa_Platform_TileNames_SendProtocolTasks.htm)|  Плитка
верхнего уровня на левой панели для рассылки задач по протоколу.  
[SettingsCard](F_Tessa_Platform_TileNames_SettingsCard.htm)|  Плитка верхнего
уровня, выводящая список карточек с настройками для открытия.  
[SettingsTypes](F_Tessa_Platform_TileNames_SettingsTypes.htm)|  Плитка,
вложенная в [CreateCard](F_Tessa_Platform_TileNames_CreateCard.htm) и
группирующая все типы карточек, относящиеся к настройкам.  
[ShowCardStorageDialog](F_Tessa_Platform_TileNames_ShowCardStorageDialog.htm)|
Плитка, вложенная в [Dialogues](F_Tessa_Platform_TileNames_Dialogues.htm) и
отображающая структуру карточки, выгруженную в файл.  
[ShowEmptyFolders](F_Tessa_Platform_TileNames_ShowEmptyFolders.htm)|  Плитка
вложенная в [ViewsOther](F_Tessa_Platform_TileNames_ViewsOther.htm) показать
пустые папки  
[ShowInaccessibleItems](F_Tessa_Platform_TileNames_ShowInaccessibleItems.htm)|
Дочерняя плитка для
[TreeSettings](F_Tessa_Platform_TileNames_TreeSettings.htm) Отобразить
недоступные элементы  
[ShowProperties](F_Tessa_Platform_TileNames_ShowProperties.htm)|  Дочерняя
плитка для [TreeSettings](F_Tessa_Platform_TileNames_TreeSettings.htm)
Отобразить свойства узла  
[ShowTree](F_Tessa_Platform_TileNames_ShowTree.htm)|  Плитка вложенная в
[ViewsOther](F_Tessa_Platform_TileNames_ViewsOther.htm) показать дерево
представлений  
[StageSourceBuild](F_Tessa_Platform_TileNames_StageSourceBuild.htm)|  Плитка
верхнего уровня. Сборка в KrStageTemplates и KrStageCommonMethods  
[SystemTypes](F_Tessa_Platform_TileNames_SystemTypes.htm)|  Плитка, вложенная
в [CreateCard](F_Tessa_Platform_TileNames_CreateCard.htm) и группирующая все
типы карточек, относящиеся к системным.  
[TemplateCard](F_Tessa_Platform_TileNames_TemplateCard.htm)|  Плитка,
вложенная в [Dialogues](F_Tessa_Platform_TileNames_Dialogues.htm) для создания
карточки по шаблону из выбранного файла.  
[TemplateCardDialog](F_Tessa_Platform_TileNames_TemplateCardDialog.htm)|
Плитка, вложенная в [Dialogues](F_Tessa_Platform_TileNames_Dialogues.htm) и
открывающая диалог создания карточки по шаблону.  
[TreeSettings](F_Tessa_Platform_TileNames_TreeSettings.htm)|  Плитка верхнего
уровня Настройки дерева рабочего места  
[ViewAllDataExport](F_Tessa_Platform_TileNames_ViewAllDataExport.htm)|  Плитка
верхнего уровня экспорт всех данных представления  
[ViewCardFromDeleted](F_Tessa_Platform_TileNames_ViewCardFromDeleted.htm)|
Плитка верхнего уровня для просмотра удалённой карточки.  
[ViewCardStorage](F_Tessa_Platform_TileNames_ViewCardStorage.htm)|  Плитка на
уровне [CardOthers](F_Tessa_Platform_TileNames_CardOthers.htm) для просмотра
содержимого карточки.  
[ViewCurrentPageExport](F_Tessa_Platform_TileNames_ViewCurrentPageExport.htm)|
Плитка верхнего уровня экспорт текущей страницы представления  
[ViewExported](F_Tessa_Platform_TileNames_ViewExported.htm)|  Плитка,
вложенная в [Dialogues](F_Tessa_Platform_TileNames_Dialogues.htm) для
просмотра карточки из выбранного файла.  
[ViewsOther](F_Tessa_Platform_TileNames_ViewsOther.htm)|  Плитка верхнего
уровня Другие для отображаения в представлениях  
[ViewStorageFromView](F_Tessa_Platform_TileNames_ViewStorageFromView.htm)|
Плитка верхнего уровня для отображения структуры карточки из представления  
[ZoomCurrentView](F_Tessa_Platform_TileNames_ZoomCurrentView.htm)|  Плитка
вложенная в [ViewsOther](F_Tessa_Platform_TileNames_ViewsOther.htm) Открыть
текущую страницу в новом окне  
## __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
