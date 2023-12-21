# DefaultExtensionHelper.SetSourceID - метод
Устанавливает местоположение контента файлов в запросе request.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared](N_Tessa_Extensions_Default_Shared.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetSourceID(
    	CardRequest request,
    	CardFileSourceType sourceType
    )
VB __Копировать
     Public Shared Sub SetSourceID ( 
    	request As CardRequest,
    	sourceType As CardFileSourceType
    )
C++ __Копировать
     public:
    static void SetSourceID(
    	CardRequest^ request, 
    	CardFileSourceType sourceType
    )
F# __Копировать
     static member SetSourceID : 
            request : CardRequest * 
            sourceType : CardFileSourceType -> unit 
#### Параметры
request [CardRequest](T_Tessa_Cards_CardRequest.htm)
    Запрос, требующий известного местоположения.
sourceType [CardFileSourceType](T_Tessa_Cards_CardFileSourceType.htm)
    Местоположение контента файлов, задаваемое в запросе.
##  __См. также
#### Ссылки
[DefaultExtensionHelper -
](T_Tessa_Extensions_Default_Shared_DefaultExtensionHelper.htm)
[Tessa.Extensions.Default.Shared - пространство
имён](N_Tessa_Extensions_Default_Shared.htm)
