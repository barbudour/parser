# IUIHost - интерфейс
Объект, предоставляющий упрощённый доступ к основным функциям платформы,
которые связаны с отображением информации пользователю.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IUIHost
VB __Копировать
     Public Interface IUIHost
C++ __Копировать
     public interface class IUIHost
F# __Копировать
     type IUIHost = interface end
##  __Методы
[CreateCardAsync](M_Tessa_UI_IUIHost_CreateCardAsync.htm)|  Создаёт карточку и
открывает её в отдельной вкладке. Запрос на создание карточки и расширения
выполняются асинхронно. Используйте метод с конструкцией await.  
---|---  
[OpenCardAsync](M_Tessa_UI_IUIHost_OpenCardAsync.htm)|  Открывает карточку или
выбирает вкладку с уже открытой карточкой, если карточка по идентификатору
cardID уже была открыта. Запрос на открытие карточки и расширения выполняются
асинхронно. Используйте метод с конструкцией await.  
[ShowCardAsync(ICardEditorModel, Func<ICardEditorModel, CancellationToken,
ValueTask<Boolean>>, ShowCardOptions,
CancellationToken)](M_Tessa_UI_IUIHost_ShowCardAsync.htm)| Отображает карточку
в новой вкладке.  
[ShowCardAsync(ICardModel, String, Func<ICardEditorModel, CancellationToken,
ValueTask<Boolean>>, ShowCardOptions,
CancellationToken)](M_Tessa_UI_IUIHost_ShowCardAsync_1.htm)| Отображает
карточку в новой вкладке.  
[ShowDialogAsync](M_Tessa_UI_IUIHost_ShowDialogAsync.htm)| Отображает
диалоговое окно с заданным содержимым и кнопками.  
[ShowFilterDialog](M_Tessa_UI_IUIHost_ShowFilterDialog.htm)| Отображает диалог
фильтрации.  
[ShowFormDialogAsync](M_Tessa_UI_IUIHost_ShowFormDialogAsync.htm)|  Отображает
диалоговое окно для формы карточки или для самой карточки. Возвращает признак
того, что диалог был отображён. Если метод возвращает false, то при выполнении
расширений возникли ошибки или расширения отменили отображение диалога.  
[ShowViewAsync](M_Tessa_UI_IUIHost_ShowViewAsync.htm)|  Открывает
представление с псевдонимом viewAlias во вкладке с заголовком displayValue. В
открываемое представление передаются параметры представления parameters.
Возвращается текущий контекст для открытой вкладки или null, если вкладка не
была открыта или не содержит контекст (кастомная вкладка).  
[ShowViewsDialogAsync](M_Tessa_UI_IUIHost_ShowViewsDialogAsync.htm)|
Отображает диалоговое окно с выбором объекта среди всех доступных
представлениям.  
##  __Методы расширения
[CreateFromTemplateAsync](M_Tessa_UI_UIExtensions_CreateFromTemplateAsync_1.htm)|
Создаёт карточку по шаблону и открывает её в новой вкладке. При создании по
шаблону используются и клиентские, и серверные расширения. Возвращает вкладку
с карточкой, созданной по шаблону, или null, если карточку не удалось создать.  
(Определяется [UIExtensions](T_Tessa_UI_UIExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
