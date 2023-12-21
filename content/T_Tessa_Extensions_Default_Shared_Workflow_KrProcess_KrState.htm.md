# KrState - структура
Cостояние согласования документа.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public readonly struct KrState : IEquatable<KrState>, 
    	IEquatable<int>
VB __Копировать
     Public Structure KrState
    	Implements IEquatable(Of KrState), IEquatable(Of Integer)
C++ __Копировать
     public value class KrState : IEquatable<KrState>, 
    	IEquatable<int>
F# __Копировать
     [<SealedAttribute>]
    type KrState = 
        struct
            inherit ValueType
            interface IEquatable<KrState>
            interface IEquatable<int>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValueType](https://learn.microsoft.com/dotnet/api/system.valuetype) __ KrState
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<KrState>, [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[Int32](https://learn.microsoft.com/dotnet/api/system.int32)>
##  __Конструкторы
[KrState](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState__ctor.htm)|
Создаёт экземпляр состояния документа.  
---|---  
## __Свойства
[ID](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState_ID.htm)|
Идентификатор местоположения.  
---|---  
## __Методы
[Equals(Int32)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState_Equals.htm)|
Indicates whether the current object is equal to another object of the same
type.  
---|---  
[Equals(KrState)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState_Equals_2.htm)|  
[Equals(Object)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState_Equals_1.htm)|  
(Переопределяет
[ValueType.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.valuetype.equals#system-
valuetype-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState_GetHashCode.htm)|  
(Переопределяет
[ValueType.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.valuetype.gethashcode#system-
valuetype-gethashcode))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IsDefault](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState_IsDefault.htm)|  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState_ToString.htm)|  
(Переопределяет
[ValueType.ToString()](https://learn.microsoft.com/dotnet/api/system.valuetype.tostring#system-
valuetype-tostring))  
[TryGetDefaultName](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState_TryGetDefaultName.htm)|  
## __Операторы
[Equality(Int32,
KrState)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState_op_Equality.htm)|  
---|---  
[Equality(KrState,
Int32)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState_op_Equality_1.htm)|  
[Equality(KrState,
KrState)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState_op_Equality_2.htm)|  
[Explicit(Int32 to
KrState)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState_op_Explicit.htm)|  
[Explicit(KrState to
Int32)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState_op_Explicit_1.htm)|  
[Inequality(Int32,
KrState)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState_op_Inequality.htm)|  
[Inequality(KrState,
Int32)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState_op_Inequality_1.htm)|  
[Inequality(KrState,
KrState)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState_op_Inequality_2.htm)|  
## __Поля
[Active](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState_Active.htm)|
На согласовании  
---|---  
[Approved](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState_Approved.htm)|
Согласован  
[Cancelled](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState_Cancelled.htm)|
Отменено  
[Declined](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState_Declined.htm)|
Отказан  
[DefaultStateNames](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState_DefaultStateNames.htm)|
Список всех стандартных названий состояний карточки.  
[DefaultStates](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState_DefaultStates.htm)|
Список всех стандартных состояния карточки.  
[Disapproved](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState_Disapproved.htm)|
Не согласован  
[Draft](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState_Draft.htm)|
Проект  
[Editing](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState_Editing.htm)|
На доработке.  
[Registered](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState_Registered.htm)|
Зарегистрирован  
[Registration](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState_Registration.htm)|
На регистрации  
[Signed](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState_Signed.htm)|
Подписан  
[Signing](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState_Signing.htm)|
На подписании  
## __Методы расширения
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
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
