# Rule - класс
Represents a rule that automatically handles incoming messages. A rule
consists of a set of conditions and exceptions that determine whether or not a
set of actions should be executed on incoming messages.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class Rule : ComplexProperty
VB __Копировать
     Public NotInheritable Class Rule
    	Inherits ComplexProperty
C++ __Копировать
     public ref class Rule sealed : public ComplexProperty
F# __Копировать
     [<SealedAttribute>]
    type Rule = 
        class
            inherit ComplexProperty
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ComplexProperty](T_Tessa_Exchange_WebServices_Data_ComplexProperty.htm) __ Rule
##  __Конструкторы
[Rule](M_Tessa_Exchange_WebServices_Data_Rule__ctor.htm)|  Initializes a new
instance of the Rule class.  
---|---  
## __Свойства
[Actions](P_Tessa_Exchange_WebServices_Data_Rule_Actions.htm)|  Gets the
actions that should be executed against incoming messages if the conditions
evaluate as true.  
---|---  
[Conditions](P_Tessa_Exchange_WebServices_Data_Rule_Conditions.htm)|  Gets the
conditions that determine whether or not this rule should be executed against
incoming messages.  
[DisplayName](P_Tessa_Exchange_WebServices_Data_Rule_DisplayName.htm)|  Gets
or sets the name of this rule as it should be displayed to the user.  
[Exceptions](P_Tessa_Exchange_WebServices_Data_Rule_Exceptions.htm)|  Gets the
exceptions that determine if this rule should be skipped even if its
conditions evaluate to true.  
[Id](P_Tessa_Exchange_WebServices_Data_Rule_Id.htm)|  Gets or sets the Id of
this rule.  
[IsEnabled](P_Tessa_Exchange_WebServices_Data_Rule_IsEnabled.htm)|  Gets or
sets a value indicating whether this rule is enabled.  
[IsInError](P_Tessa_Exchange_WebServices_Data_Rule_IsInError.htm)|  Gets or
sets a value indicating whether this rule has errors. A rule that is in error
cannot be processed unless it is updated and the error is corrected.  
[IsNotSupported](P_Tessa_Exchange_WebServices_Data_Rule_IsNotSupported.htm)|
Gets a value indicating whether this rule can be modified via EWS. If
IsNotSupported is true, the rule cannot be modified via EWS.  
[Priority](P_Tessa_Exchange_WebServices_Data_Rule_Priority.htm)|  Gets or sets
the priority of this rule, which determines its execution order.  
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
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
