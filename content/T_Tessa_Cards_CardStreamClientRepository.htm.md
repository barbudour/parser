# CardStreamClientRepository - класс
Репозиторий для потокового управления карточками на клиенте.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardStreamClientRepository : ICardStreamClientRepository
VB __Копировать
     Public NotInheritable Class CardStreamClientRepository
    	Implements ICardStreamClientRepository
C++ __Копировать
     public ref class CardStreamClientRepository sealed : ICardStreamClientRepository
F# __Копировать
     [<SealedAttribute>]
    type CardStreamClientRepository = 
        class
            interface ICardStreamClientRepository
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardStreamClientRepository
Implements
    [ICardStreamClientRepository](T_Tessa_Cards_ICardStreamClientRepository.htm)
##  __Конструкторы
[CardStreamClientRepository](M_Tessa_Cards_CardStreamClientRepository__ctor.htm)|
Создаёт новый экземпляр класса с указанием компонентов репозитория.  
---|---  
## __Методы
[CreateDefault](M_Tessa_Cards_CardStreamClientRepository_CreateDefault.htm)|
Создаёт экземпляр репозитория с конфигурацией клиентских компонентов по
умолчанию, с указанием сервиса для потокового управления карточками.  
---|---  
[CreateExtended](M_Tessa_Cards_CardStreamClientRepository_CreateExtended.htm)|
Создаёт экземпляр репозитория с расширенной конфигурацией клиентских
компонентов по умолчанию, с указанием контейнера с используемыми расширениями
и сервиса для потокового управления карточками.  
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
[GetFileContentAsync](M_Tessa_Cards_CardStreamClientRepository_GetFileContentAsync.htm)|
Получает контент версии файла.  
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
[StoreAsync](M_Tessa_Cards_CardStreamClientRepository_StoreAsync.htm)|
Сохраняет карточку с контентом файлов, которые упаковываются в поток карточки
перед отправкой на сервер.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[GenerateExportAsync](M_Tessa_Cards_CardExtensions_GenerateExportAsync.htm)|
Создаёт файл по заданному шаблону и возвращает контент созданного файла и
ответ на запрос на создание.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
---|---  
[GenerateFileFromTemplateAsync](M_Tessa_Cards_CardExtensions_GenerateFileFromTemplateAsync.htm)|
Создаёт файл по заданному шаблону и возвращает контент созданного файла и
ответ на запрос на создание.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
