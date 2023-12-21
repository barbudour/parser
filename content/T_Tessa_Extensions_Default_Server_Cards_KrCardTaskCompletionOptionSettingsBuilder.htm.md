# KrCardTaskCompletionOptionSettingsBuilder - класс
Предоставляет билдер объектов типа
[CardTaskCompletionOptionSettings](T_Tessa_Cards_CardTaskCompletionOptionSettings.htm)
реализующий функционал специфичный для параметров используемых в маршрутах.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Cards](N_Tessa_Extensions_Default_Server_Cards.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public class KrCardTaskCompletionOptionSettingsBuilder : CardTaskCompletionOptionSettingsBuilder
VB __Копировать
     Public Class KrCardTaskCompletionOptionSettingsBuilder
    	Inherits CardTaskCompletionOptionSettingsBuilder
C++ __Копировать
     public ref class KrCardTaskCompletionOptionSettingsBuilder : public CardTaskCompletionOptionSettingsBuilder
F# __Копировать
     type KrCardTaskCompletionOptionSettingsBuilder = 
        class
            inherit CardTaskCompletionOptionSettingsBuilder
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardTaskCompletionOptionSettingsBuilder](T_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder.htm) __ KrCardTaskCompletionOptionSettingsBuilder
##  __Конструкторы
[KrCardTaskCompletionOptionSettingsBuilder](M_Tessa_Extensions_Default_Server_Cards_KrCardTaskCompletionOptionSettingsBuilder__ctor.htm)|
Инициализирует новый экземпляр класса
KrCardTaskCompletionOptionSettingsBuilder.  
---|---  
## __Методы
[AddButton](M_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder_AddButton.htm)|
Добавляет кнопку в создаваемый объект.  
(Унаследован от
[CardTaskCompletionOptionSettingsBuilder](T_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder.htm))  
---|---  
[BuildAsync](M_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder_BuildAsync.htm)|
Создаёт итоговый объект
[CardTaskCompletionOptionSettings](T_Tessa_Cards_CardTaskCompletionOptionSettings.htm).  
(Унаследован от
[CardTaskCompletionOptionSettingsBuilder](T_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder.htm))  
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
[ModifyResultAsync](M_Tessa_Extensions_Default_Server_Cards_KrCardTaskCompletionOptionSettingsBuilder_ModifyResultAsync.htm)|
Метод для модификации результата билдера, вызывается при вызове
[BuildAsync(IValidationResultBuilder,
CancellationToken)](M_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder_BuildAsync.htm).  
(Переопределяет
[CardTaskCompletionOptionSettingsBuilder.ModifyResultAsync(CardTaskCompletionOptionSettings,
IValidationResultBuilder,
CancellationToken)](M_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder_ModifyResultAsync.htm))  
[SetCardNewMethod](M_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder_SetCardNewMethod.htm)|
Устанавливает способ создания карточки диалога.  
(Унаследован от
[CardTaskCompletionOptionSettingsBuilder](T_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder.htm))  
[SetCompletionOption](M_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder_SetCompletionOption.htm)|
Устанавливает вариант завершения, для которого создается настройка.  
(Унаследован от
[CardTaskCompletionOptionSettingsBuilder](T_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder.htm))  
[SetDialogAlias](M_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder_SetDialogAlias.htm)|
Устанавливает уникальный алиас диалога.  
(Унаследован от
[CardTaskCompletionOptionSettingsBuilder](T_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder.htm))  
[SetDialogCaption](M_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder_SetDialogCaption.htm)|
Устанавливает отображаемое имя диалога.  
(Унаследован от
[CardTaskCompletionOptionSettingsBuilder](T_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder.htm))  
[SetDialogName](M_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder_SetDialogName.htm)|
Устанавливает имя диалога.  
(Унаследован от
[CardTaskCompletionOptionSettingsBuilder](T_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder.htm))  
[SetDialogType](M_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder_SetDialogType.htm)|
Устанавливает тип карточки диалога.  
(Унаследован от
[CardTaskCompletionOptionSettingsBuilder](T_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder.htm))  
[SetIsCloseWithoutConfirmation](M_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder_SetIsCloseWithoutConfirmation.htm)|
Устанавливает значение флага "Не предупреждать при закрытии диалога без
изменений".  
(Унаследован от
[CardTaskCompletionOptionSettingsBuilder](T_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder.htm))  
[SetKeepFiles](M_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder_SetKeepFiles.htm)|
Устанавливает значение флага "Сохранять файлы после завершения диалога".  
(Унаследован от
[CardTaskCompletionOptionSettingsBuilder](T_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder.htm))  
[SetNotDisplayTabs](M_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder_SetNotDisplayTabs.htm)|
Устанавливает значение флага "Не выводить вкладки".  
(Унаследован от
[CardTaskCompletionOptionSettingsBuilder](T_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder.htm))  
[SetOpenMode](M_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder_SetOpenMode.htm)|
Устанавливает режим открытия диалога.  
(Унаследован от
[CardTaskCompletionOptionSettingsBuilder](T_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder.htm))  
[SetStoreMode](M_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder_SetStoreMode.htm)|
Устанавливает режим сохранения диалога.  
(Унаследован от
[CardTaskCompletionOptionSettingsBuilder](T_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder.htm))  
[SetTaskButtonCaption](M_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder_SetTaskButtonCaption.htm)|
Устанавливает имя кнопки диалога, которая будет отображаться в задании для
данного диалога.  
(Унаследован от
[CardTaskCompletionOptionSettingsBuilder](T_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
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
[Tessa.Extensions.Default.Server.Cards - пространство
имён](N_Tessa_Extensions_Default_Server_Cards.htm)
