# NotificationSettingsUIExtension.Saving - метод
##  __Список перегрузок
[Saving(ICardUIExtensionContext)](M_Tessa_UI_Cards_CardUIExtension_Saving.htm)|
Выполняется перед сохранением карточки, которое вызвано любым способом из
редактора карточек [Tessa.UI.Cards.ICardEditorModel], в том числе при
завершении задания или закрытии вкладки с сохранением. В метод передаётся
пакет карточки, изменённый перед сохранением, а также исходный объект
[Tessa.UI.Cards.ICardModel]. Метод позволяет выполнить любые подготовительные
действия, в т.ч. затрагивающие изменение файлов карточки, вследствие чего
будет применено обычное или потоковое сохранение карточки. Выполнение
производится в том же потоке, в которой вызывалось сохранение карточки. Обычно
это поток, асинхронный по отношению к UI.  
---|---  
[Saving(IMySettingsExtensionContext)](M_Tessa_Extensions_Platform_Client_UI_NotificationSettingsUIExtension_Saving.htm)|  
## __См. также
#### Ссылки
[NotificationSettingsUIExtension -
](T_Tessa_Extensions_Platform_Client_UI_NotificationSettingsUIExtension.htm)
[Tessa.Extensions.Platform.Client.UI - пространство
имён](N_Tessa_Extensions_Platform_Client_UI.htm)
