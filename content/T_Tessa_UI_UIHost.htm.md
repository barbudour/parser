# UIHost - класс
Объект, предоставляющий упрощённый доступ к основным функциям платформы,
которые связаны с отображением информации пользователю.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class UIHost : IUIHost
VB __Копировать
     Public NotInheritable Class UIHost
    	Implements IUIHost
C++ __Копировать
     public ref class UIHost sealed : IUIHost
F# __Копировать
     [<SealedAttribute>]
    type UIHost = 
        class
            interface IUIHost
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ UIHost
Implements
    [IUIHost](T_Tessa_UI_IUIHost.htm)
##  __Конструкторы
[UIHost](M_Tessa_UI_UIHost__ctor.htm)|  Инициализирует новый экземпляр класса
UIHost.  
---|---  
## __Методы
[CreateCardAsync](M_Tessa_UI_UIHost_CreateCardAsync.htm)|  Создаёт карточку и
открывает её в отдельной вкладке. Запрос на создание карточки и расширения
выполняются асинхронно. Используйте метод с конструкцией await.  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OpenCardAsync](M_Tessa_UI_UIHost_OpenCardAsync.htm)|  Открывает карточку или
выбирает вкладку с уже открытой карточкой, если карточка по идентификатору
cardID уже была открыта. Запрос на открытие карточки и расширения выполняются
асинхронно. Используйте метод с конструкцией await.  
[ShowCardAsync(ICardEditorModel, Func<ICardEditorModel, CancellationToken,
ValueTask<Boolean>>, ShowCardOptions,
CancellationToken)](M_Tessa_UI_UIHost_ShowCardAsync.htm)| Отображает карточку
в новой вкладке.  
[ShowCardAsync(ICardModel, String, Func<ICardEditorModel, CancellationToken,
ValueTask<Boolean>>, ShowCardOptions,
CancellationToken)](M_Tessa_UI_UIHost_ShowCardAsync_1.htm)| Отображает
карточку в новой вкладке.  
[ShowDialogAsync](M_Tessa_UI_UIHost_ShowDialogAsync.htm)| Отображает
диалоговое окно с заданным содержимым и кнопками.  
[ShowFilterDialog](M_Tessa_UI_UIHost_ShowFilterDialog.htm)| Отображает диалог
фильтрации.  
[ShowFormDialogAsync](M_Tessa_UI_UIHost_ShowFormDialogAsync.htm)|  Отображает
диалоговое окно для формы карточки или для самой карточки. Возвращает признак
того, что диалог был отображён. Если метод возвращает false, то при выполнении
расширений возникли ошибки или расширения отменили отображение диалога.  
[ShowViewAsync](M_Tessa_UI_UIHost_ShowViewAsync.htm)|  Открывает представление
с псевдонимом viewAlias во вкладке с заголовком displayValue. В открываемое
представление передаются параметры представления parameters. Возвращается
текущий контекст для открытой вкладки или null, если вкладка не была открыта
или не содержит контекст (кастомная вкладка).  
[ShowViewsDialogAsync](M_Tessa_UI_UIHost_ShowViewsDialogAsync.htm)| Отображает
диалоговое окно с выбором объекта среди всех доступных представлениям.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[CreateFromTemplateAsync](M_Tessa_UI_UIExtensions_CreateFromTemplateAsync_1.htm)|
Создаёт карточку по шаблону и открывает её в новой вкладке. При создании по
шаблону используются и клиентские, и серверные расширения. Возвращает вкладку
с карточкой, созданной по шаблону, или null, если карточку не удалось создать.  
(Определяется [UIExtensions](T_Tessa_UI_UIExtensions.htm))  
---|---  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
