# KrStageState - структура
Состояние этапа.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public readonly struct KrStageState : IEquatable<KrStageState>, 
    	IEquatable<int>
VB __Копировать
     Public Structure KrStageState
    	Implements IEquatable(Of KrStageState), IEquatable(Of Integer)
C++ __Копировать
     public value class KrStageState : IEquatable<KrStageState>, 
    	IEquatable<int>
F# __Копировать
     [<SealedAttribute>]
    type KrStageState = 
        struct
            inherit ValueType
            interface IEquatable<KrStageState>
            interface IEquatable<int>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValueType](https://learn.microsoft.com/dotnet/api/system.valuetype) __ KrStageState
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<KrStageState>, [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[Int32](https://learn.microsoft.com/dotnet/api/system.int32)>
##  __Конструкторы
[KrStageState](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStageState__ctor.htm)|
Создаёт экземпляр состояния с указанием его идентификатора.  
---|---  
## __Свойства
[ID](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStageState_ID.htm)|
Идентификатор состояния.  
---|---  
## __Методы
[Equals(Int32)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStageState_Equals.htm)|  
---|---  
[Equals(KrStageState)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStageState_Equals_2.htm)|
Indicates whether the current object is equal to another object of the same
type.  
[Equals(Object)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStageState_Equals_1.htm)|  
(Переопределяет
[ValueType.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.valuetype.equals#system-
valuetype-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStageState_GetHashCode.htm)|  
(Переопределяет
[ValueType.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.valuetype.gethashcode#system-
valuetype-gethashcode))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IsDefault](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStageState_IsDefault.htm)|
Возвращает знчаение показывающее, является ли состояние стандартным или нет.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStageState_ToString.htm)|  
(Переопределяет
[ValueType.ToString()](https://learn.microsoft.com/dotnet/api/system.valuetype.tostring#system-
valuetype-tostring))  
[TryGetDefaultName](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStageState_TryGetDefaultName.htm)|
Вовзращает стандартное название состояния в соответствии с его идентификатором
или значение по умолчанию для типа, если состоянию не соответсвует стандартное
название.  
## __Операторы
[Equality(Int32,
KrStageState)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStageState_op_Equality.htm)|  
---|---  
[Equality(KrStageState,
Int32)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStageState_op_Equality_1.htm)|  
[Equality(KrStageState,
KrStageState)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStageState_op_Equality_2.htm)|  
[Explicit(Int32 to
KrStageState)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStageState_op_Explicit.htm)|  
[Explicit(KrStageState to
Int32)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStageState_op_Explicit_1.htm)|  
[Inequality(Int32,
KrStageState)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStageState_op_Inequality.htm)|  
[Inequality(KrStageState,
Int32)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStageState_op_Inequality_1.htm)|  
[Inequality(KrStageState,
KrStageState)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStageState_op_Inequality_2.htm)|  
## __Поля
[Active](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStageState_Active.htm)|
Активен.  
---|---  
[Completed](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStageState_Completed.htm)|
Завершен.  
[DefaultStateNames](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStageState_DefaultStateNames.htm)|
Список стандартных названий состояний этапа.  
[DefaultStates](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStageState_DefaultStates.htm)|
Список стандартных состояний этапа.  
[Inactive](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStageState_Inactive.htm)|
Не активен / не запущен.  
[Skipped](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStageState_Skipped.htm)|
Пропущен.  
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
