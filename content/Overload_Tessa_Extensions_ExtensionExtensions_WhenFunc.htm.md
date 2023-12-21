# ExtensionExtensions.WhenFunc - метод
##  __Список перегрузок
[WhenFunc(IExtensionPolicyContainer, Func<IExtensionContext,
Boolean>)](M_Tessa_Extensions_ExtensionExtensions_WhenFunc.htm)|  Регистрирует
политику фильтрации выполнения методов любых расширений
[IExtension](T_Tessa_Extensions_IExtension.htm) в соответствии с функцией
isAllowedFunc, которая проверяет контекст расширений. Если зарегистрировано
несколько политик, то должны выполняться все из них.  
---|---  
[WhenFunc<TContext>(IExtensionPolicyContainer, Func<TContext,
Boolean>)](M_Tessa_Extensions_ExtensionExtensions_WhenFunc__1.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[IExtension](T_Tessa_Extensions_IExtension.htm), принимающих указанный тип
контекста TContext, в соответствии с функцией isAllowedFunc, которая проверяет
контекст расширений. Если зарегистрировано несколько политик, то должны
выполняться все из них. Если тип контекста отличается от указанного, то
политика игнорируется, т.е. возвращает true.  
## __См. также
#### Ссылки
[ExtensionExtensions - ](T_Tessa_Extensions_ExtensionExtensions.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
