# ActionHistoryDescriptionProvider - класс
Объект, возвращающий текстовое описание действия с карточкой.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class ActionHistoryDescriptionProvider : IActionHistoryDescriptionProvider
VB __Копировать
     Public Class ActionHistoryDescriptionProvider
    	Implements IActionHistoryDescriptionProvider
C++ __Копировать
     public ref class ActionHistoryDescriptionProvider : IActionHistoryDescriptionProvider
F# __Копировать
     type ActionHistoryDescriptionProvider = 
        class
            interface IActionHistoryDescriptionProvider
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ActionHistoryDescriptionProvider
Implements
    [IActionHistoryDescriptionProvider](T_Tessa_Platform_Runtime_IActionHistoryDescriptionProvider.htm)
##  __Заметки
Вы можете создать наследник класса, где в конструкторе добавить или изменить
функцию генерации описания в свойстве
[DescriptionFunctionsByActionType](P_Tessa_Platform_Runtime_ActionHistoryDescriptionProvider_DescriptionFunctionsByActionType.htm).
Вы также можете переопределить функцию
[BuildDescriptionAsync(IActionHistoryDescriptionContext)](M_Tessa_Platform_Runtime_ActionHistoryDescriptionProvider_BuildDescriptionAsync.htm),
которая по умолчанию использует свойство
[DescriptionFunctionsByActionType](P_Tessa_Platform_Runtime_ActionHistoryDescriptionProvider_DescriptionFunctionsByActionType.htm).
## __Конструкторы
[ActionHistoryDescriptionProvider](M_Tessa_Platform_Runtime_ActionHistoryDescriptionProvider__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[DescriptionBuilder](P_Tessa_Platform_Runtime_ActionHistoryDescriptionProvider_DescriptionBuilder.htm)|
Объект, выполняющий построение текстового описания.  
---|---  
[DescriptionFunctionsByActionType](P_Tessa_Platform_Runtime_ActionHistoryDescriptionProvider_DescriptionFunctionsByActionType.htm)|
Функции создания описания, выбираемые в зависимости от типа действия
[ActionType](T_Tessa_Platform_Runtime_ActionType.htm).  
[DescriptionSerializer](P_Tessa_Platform_Runtime_ActionHistoryDescriptionProvider_DescriptionSerializer.htm)|
Объект, управляющий сериализацией описаний ошибок
[IErrorDescription](T_Tessa_Platform_Runtime_IErrorDescription.htm).  
## __Методы
[BuildDescriptionAsync](M_Tessa_Platform_Runtime_ActionHistoryDescriptionProvider_BuildDescriptionAsync.htm)|
Выполняет построение описания для действий в истории.  
---|---  
[CreateContext](M_Tessa_Platform_Runtime_ActionHistoryDescriptionProvider_CreateContext.htm)|
Создаёт контекст, используемый в методе
[BuildDescriptionAsync(IActionHistoryDescriptionContext)](M_Tessa_Platform_Runtime_ActionHistoryDescriptionProvider_BuildDescriptionAsync.htm).  
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
[GetRecordDescriptionAsync](M_Tessa_Platform_Runtime_ActionHistoryDescriptionProvider_GetRecordDescriptionAsync.htm)|
Возвращает текстовое описание действия с карточкой.  
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
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
