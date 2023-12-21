# KrStageTypeUIHandlerContext - класс
Контекст расширений
[IStageTypeUIHandler](T_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_IStageTypeUIHandler.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.UI.KrProcess.StageHandlers](N_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrStageTypeUIHandlerContext : IKrStageTypeUIHandlerContext, 
    	IExtensionContext
VB __Копировать
     Public NotInheritable Class KrStageTypeUIHandlerContext
    	Implements IKrStageTypeUIHandlerContext, IExtensionContext
C++ __Копировать
     public ref class KrStageTypeUIHandlerContext sealed : IKrStageTypeUIHandlerContext, 
    	IExtensionContext
F# __Копировать
     [<SealedAttribute>]
    type KrStageTypeUIHandlerContext = 
        class
            interface IKrStageTypeUIHandlerContext
            interface IExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrStageTypeUIHandlerContext
Implements
    [IKrStageTypeUIHandlerContext](T_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_IKrStageTypeUIHandlerContext.htm), [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Конструкторы
[KrStageTypeUIHandlerContext](M_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_KrStageTypeUIHandlerContext__ctor.htm)|
Инициализирует новый экземпляр класса.  
---|---  
## __Свойства
[Action](P_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_KrStageTypeUIHandlerContext_Action.htm)|
Действие со строкой
[Row](P_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_IKrStageTypeUIHandlerContext_Row.htm)
или значение null, если выполняется валидация строки с параметрами этапа
([Validate(IKrStageTypeUIHandlerContext)](M_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_IStageTypeUIHandler_Validate.htm)).  
---|---  
[CancellationToken](P_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_KrStageTypeUIHandlerContext_CancellationToken.htm)|  
[CardModel](P_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_KrStageTypeUIHandlerContext_CardModel.htm)|
Модель карточки, в которой расположена строка
[Row](P_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_IKrStageTypeUIHandlerContext_Row.htm).  
[Control](P_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_KrStageTypeUIHandlerContext_Control.htm)|
Элемент управления, в рамках которого выполняется событие или значение null,
если выполняется валидация строки с параметрами этапа
([Validate(IKrStageTypeUIHandlerContext)](M_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_IStageTypeUIHandler_Validate.htm)).  
[Row](P_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_KrStageTypeUIHandlerContext_Row.htm)|
Строка карточки с параметрами этапа, с которой производится действие.  
[RowModel](P_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_KrStageTypeUIHandlerContext_RowModel.htm)|
Модель строки
[Row](P_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_IKrStageTypeUIHandlerContext_Row.htm)
с параметрами этапа вместе с формой.  
[SettingsForms](P_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_KrStageTypeUIHandlerContext_SettingsForms.htm)|
Коллекция, содержащая формы из типа карточки настроек текущего этапа.  
[StageTypeID](P_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_KrStageTypeUIHandlerContext_StageTypeID.htm)|
Идентификатор типа этапа.  
[ValidationResult](P_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_KrStageTypeUIHandlerContext_ValidationResult.htm)|  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
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
[Tessa.Extensions.Default.Client.UI.KrProcess.StageHandlers - пространство
имён](N_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers.htm)
