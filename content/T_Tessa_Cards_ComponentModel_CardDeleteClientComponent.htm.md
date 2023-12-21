# CardDeleteClientComponent - класс
Компонент, выполняющий удаление карточки посредством обращения к сервису для
управления карточками.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardDeleteClientComponent : ICardDeleteComponent
VB __Копировать
     Public NotInheritable Class CardDeleteClientComponent
    	Implements ICardDeleteComponent
C++ __Копировать
     public ref class CardDeleteClientComponent sealed : ICardDeleteComponent
F# __Копировать
     [<SealedAttribute>]
    type CardDeleteClientComponent = 
        class
            interface ICardDeleteComponent
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardDeleteClientComponent
Implements
    [ICardDeleteComponent](T_Tessa_Cards_ComponentModel_ICardDeleteComponent.htm)
##  __Конструкторы
[CardDeleteClientComponent](M_Tessa_Cards_ComponentModel_CardDeleteClientComponent__ctor.htm)|
Создаёт экземпляр класса с указанием сервиса для управления карточками.  
---|---  
## __Свойства
[TransactionStrategy](P_Tessa_Cards_ComponentModel_CardDeleteClientComponent_TransactionStrategy.htm)|
Стратегия обеспечения блокировок и выполнения транзакций, используемая
сервисом, или null, если стратегия не используется, например, на клиенте.  
---|---  
## __Методы
[DeleteAsync](M_Tessa_Cards_ComponentModel_CardDeleteClientComponent_DeleteAsync.htm)|
Удаляет карточку.  
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
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
